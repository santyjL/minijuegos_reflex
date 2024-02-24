/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext } from "react"
import { EventLoopContext } from "/utils/context"
import { Event, isTrue } from "/utils/state"
import { Button, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, Text } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import { getEventURL } from "/utils/state.js"




export function Fragment_fd0e7cb8f9fb4669a6805377d925fba0 () {
  const [addEvents, connectError] = useContext(EventLoopContext);


  return (
    <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <Modal isOpen={connectError !== null}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Connection Error`}
</ModalHeader>
  <ModalBody>
  <Text>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {getEventURL().href}
</Text>
</ModalBody>
</ModalContent>
</ModalOverlay>
</Modal>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export function Button_1e8c0375e28b2af9d011a4a0800c839a () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_3d372f04947bdeeec4304e6cac8d0020 = useCallback((_e) => addEvents([Event("_redirect", {path:`/principal`,external:false})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_3d372f04947bdeeec4304e6cac8d0020} sx={{"borderRadius": "0.9em", "background": "#FF5C00", "border": "1px solid #000", "boxShadow": "2px 2px 2px 0px #32135A", "fontSize": "1.4em"}}>
  {`Regresar al Menú`}
</Button>
  )
}

export function Button_0ff058bfa0b3ebb82679fb2a2bef29fd () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_812e70f76cb7df4cacb6dac344fc8c45 = useCallback((_e) => addEvents([Event("_redirect", {path:`/Encuentra_el_numero`,external:false})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_812e70f76cb7df4cacb6dac344fc8c45} sx={{"borderRadius": "0.9em", "background": "#FF5C00", "border": "1px solid #000", "boxShadow": "2px 2px 2px 0px #32135A", "fontSize": "1.4em"}}>
  {`Nueva Partida`}
</Button>
  )
}

export function Button_ecf1aea8eedf74dec17895284b469037 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_cf75bd20132ef30404764ac9fca70a1d = useCallback((_e) => addEvents([Event("_redirect", {path:`/piedra_papel_tijeras_lagarto_spock`,external:false})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_cf75bd20132ef30404764ac9fca70a1d} sx={{"borderRadius": "0.9em", "background": "#FF5C00", "border": "1px solid #000", "boxShadow": "2px 2px 2px 0px #32135A", "fontSize": "1.4em"}}>
  {`Nueva Partida`}
</Button>
  )
}
