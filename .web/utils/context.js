import { createContext, useContext, useMemo, useReducer, useState } from "react"
import { applyDelta, Event, hydrateClientStorage, useEventLoop, refs } from "/utils/state.js"

export const initialState = {"state": {"is_hydrated": false, "router": {"session": {"client_token": "", "client_ip": "", "session_id": ""}, "headers": {"host": "", "origin": "", "upgrade": "", "connection": "", "pragma": "", "cache_control": "", "user_agent": "", "sec_websocket_version": "", "sec_websocket_key": "", "sec_websocket_extensions": "", "accept_encoding": "", "accept_language": ""}, "page": {"host": "", "path": "", "raw_path": "", "full_path": "", "full_raw_path": "", "params": {}}}}, "state.estados": {"jugada_jugador": "❓", "jugada_npc": "❓", "jugadas_jugador": "❓", "jugadas_npc": "❓", "lista": ["🥌", "📋", "✂", "🦎", "🖖"], "puntuacion_jugador": 0, "puntuacion_npc": 0, "puntuaciones_jugador": 0, "puntuaciones_npc": 0}, "state.tic_tac_toe_state": {"ganador": null, "jugador": "❌", "jugador_puntuacion": 0, "matriz": [["", "", ""], ["", "", ""], ["", "", ""]], "npc_puntuacion": 0, "puntuacion_jugador": 0, "puntuacion_npc": 0}, "state.count": {"count": 0, "estado": "¡¡¡¡!!!", "get_count": 0, "get_estado": "¡¡¡¡!!!", "intentos": 5, "num": 82}}

export const ColorModeContext = createContext(null);
export const UploadFilesContext = createContext(null);
export const DispatchContext = createContext(null);
export const StateContexts = {
  state: createContext(null),
  state__estados: createContext(null),
  state__tic_tac_toe_state: createContext(null),
  state__count: createContext(null),
}
export const EventLoopContext = createContext(null);
export const clientStorage = {"cookies": {}, "local_storage": {}}

export const onLoadInternalEvent = () => [Event('state.on_load_internal')]

export const initialEvents = () => [
    Event('state.hydrate', hydrateClientStorage(clientStorage)),
    ...onLoadInternalEvent()
]

export const isDevMode = true

export function UploadFilesProvider({ children }) {
  const [filesById, setFilesById] = useState({})
  refs["__clear_selected_files"] = (id) => setFilesById(filesById => {
    const newFilesById = {...filesById}
    delete newFilesById[id]
    return newFilesById
  })
  return (
    <UploadFilesContext.Provider value={[filesById, setFilesById]}>
      {children}
    </UploadFilesContext.Provider>
  )
}

export function EventLoopProvider({ children }) {
  const dispatch = useContext(DispatchContext)
  const [addEvents, connectError] = useEventLoop(
    dispatch,
    initialEvents,
    clientStorage,
  )
  return (
    <EventLoopContext.Provider value={[addEvents, connectError]}>
      {children}
    </EventLoopContext.Provider>
  )
}

export function StateProvider({ children }) {
  const [state, dispatch_state] = useReducer(applyDelta, initialState["state"])
  const [state__estados, dispatch_state__estados] = useReducer(applyDelta, initialState["state.estados"])
  const [state__tic_tac_toe_state, dispatch_state__tic_tac_toe_state] = useReducer(applyDelta, initialState["state.tic_tac_toe_state"])
  const [state__count, dispatch_state__count] = useReducer(applyDelta, initialState["state.count"])
  const dispatchers = useMemo(() => {
    return {
      "state": dispatch_state,
      "state.estados": dispatch_state__estados,
      "state.tic_tac_toe_state": dispatch_state__tic_tac_toe_state,
      "state.count": dispatch_state__count,
    }
  }, [])

  return (
    <StateContexts.state.Provider value={ state }>
    <StateContexts.state__estados.Provider value={ state__estados }>
    <StateContexts.state__tic_tac_toe_state.Provider value={ state__tic_tac_toe_state }>
    <StateContexts.state__count.Provider value={ state__count }>
      <DispatchContext.Provider value={dispatchers}>
        {children}
      </DispatchContext.Provider>
    </StateContexts.state__count.Provider>
    </StateContexts.state__tic_tac_toe_state.Provider>
    </StateContexts.state__estados.Provider>
    </StateContexts.state.Provider>
  )
}