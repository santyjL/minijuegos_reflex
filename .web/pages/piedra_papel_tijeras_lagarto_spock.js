/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Box, Button, Center, Heading, HStack, Image as ChakraImage, Link, Spacer, Text, VStack } from "@chakra-ui/react"
import NextLink from "next/link"
import "focus-visible/dist/focus-visible"
import { EventLoopContext, StateContexts } from "/utils/context"
import { Event } from "/utils/state"
import NextHead from "next/head"



export function Button_05b70e762d6a808a6ceb837a1ccd10c3 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_d5f9a04447965b5593845da192e224f8 = useCallback((_e) => addEvents([Event("state.estados.piedra", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_d5f9a04447965b5593845da192e224f8} sx={{"borderRadius": "10em", "background": "#32135A", "border": "1px solid #000", "boxShadow": "2px 2x 2px 0px #FF5C00", "width": "50%"}}>
  <Text sx={{"fontSize": "1.4em", "color": "#FFFFFF"}}>
  {`🥌`}
</Text>
</Button>
  )
}

export function Button_1dd91b1a1af538459f585273b2710bef () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_5722ac56ccd71a3ca0db0242a9c1504a = useCallback((_e) => addEvents([Event("state.estados.tijeras", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_5722ac56ccd71a3ca0db0242a9c1504a} sx={{"borderRadius": "10em", "background": "#32135A", "border": "1px solid #000", "boxShadow": "2px 2x 2px 0px #FF5C00", "width": "50%"}}>
  <Text sx={{"fontSize": "1.4em", "color": "#FFFFFF"}}>
  {`✂`}
</Text>
</Button>
  )
}

export function Button_3817651f523055b741ad9e694f2fa789 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_7631653a5c65880ee2c81c24dfca43d4 = useCallback((_e) => addEvents([Event("state.estados.spock", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_7631653a5c65880ee2c81c24dfca43d4} sx={{"borderRadius": "10em", "background": "#32135A", "border": "1px solid #000", "boxShadow": "2px 2x 2px 0px #FF5C00", "width": "50%"}}>
  <Text sx={{"fontSize": "1.4em", "color": "#FFFFFF"}}>
  {`🖖`}
</Text>
</Button>
  )
}

export function Heading_6e589d0c72e4ff4f97352390da89ca7b () {
  const state__estados = useContext(StateContexts.state__estados)


  return (
    <Heading sx={{"fontSize": "13.5em", "padding": "0.3em"}}>
  {state__estados.jugadas_jugador}
</Heading>
  )
}

export function Text_de4a4940a1e23bbc02e87e1cb88e4fa5 () {
  const state__estados = useContext(StateContexts.state__estados)


  return (
    <Text as={`span`} sx={{"color": "blue", "fontWeight": "bold"}}>
  {`${state__estados.puntuacion_npc}`}
</Text>
  )
}

export function Heading_6429a6a857b9b703b639ec0ba51dc3d2 () {
  const state__estados = useContext(StateContexts.state__estados)


  return (
    <Heading sx={{"fontSize": "13.5em", "padding": "0.3em"}}>
  {state__estados.jugadas_npc}
</Heading>
  )
}

export function Button_8124dab5d6f22fa178e62c1544fe6d26 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_efc72ba2d11df242b0f6e1ecc7a550bb = useCallback((_e) => addEvents([Event("state.estados.papel", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_efc72ba2d11df242b0f6e1ecc7a550bb} sx={{"borderRadius": "10em", "background": "#32135A", "border": "1px solid #000", "boxShadow": "2px 2x 2px 0px #FF5C00", "width": "50%"}}>
  <Text sx={{"fontSize": "1.4em", "color": "#FFFFFF"}}>
  {`📋`}
</Text>
</Button>
  )
}

export function Button_258adb2cf5ba98bbc099f86f06b59840 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_5dc9a6e04d5d353fc296c2721f177e1f = useCallback((_e) => addEvents([Event("state.estados.lagarto", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_5dc9a6e04d5d353fc296c2721f177e1f} sx={{"borderRadius": "10em", "background": "#32135A", "border": "1px solid #000", "boxShadow": "2px 2x 2px 0px #FF5C00", "width": "50%"}}>
  <Text sx={{"fontSize": "1.4em", "color": "#FFFFFF"}}>
  {`🦎`}
</Text>
</Button>
  )
}

export function Text_6ad1d12f9b122afabc4a8d700c2d86a3 () {
  const state__estados = useContext(StateContexts.state__estados)


  return (
    <Text as={`span`} sx={{"color": "blue", "fontWeight": "bold"}}>
  {`${state__estados.puntuacion_jugador}`}
</Text>
  )
}

export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <Box sx={{"bg": "#292833", "backgroundSize": "cover", "height": "100vh"}}>
  <Box sx={{"bg": "#FF5C00", "border": "1px solid #000"}}>
  <HStack>
  <Link as={NextLink} href={`/principal`}>
  <HStack>
  <Heading size={`lg`} sx={{"color": "#000000"}}>
  {`Game`}
</Heading>
  <Heading size={`lg`} sx={{"color": "#FFFFFF"}}>
  {`Mini`}
</Heading>
  <Heading size={`lg`} sx={{"color": "#FFFFFF"}}>
  {`⭐`}
</Heading>
</HStack>
</Link>
  <Spacer/>
  <Link as={NextLink} href={`https://github.com/santyjL/minijuegos_reflex`} isExternal={true}>
  <ChakraImage src={`/github icon.png`} sx={{"width": "3.6em", "height": "100%"}}/>
</Link>
</HStack>
</Box>
  <Center>
  <HStack spacing={`6em`} sx={{"margin": "3em"}}>
  <VStack>
  <Text sx={{"fontSize": "1.4em"}}>
  <Text as={`span`} sx={{"color": "#FFFFFF"}}>
  {`puntuación : `}
</Text>
  <Text_6ad1d12f9b122afabc4a8d700c2d86a3/>
</Text>
  <Box sx={{"borderRadius": "0.9em", "background": "#FF5C00", "marginX": "1.5em", "marginY": "1em", "padding": "0.8", "border": "1px solid #000", "boxShadow": "2px 2px 2px 0px #32135A", "width": "100%"}}>
  <Center>
  <Heading_6e589d0c72e4ff4f97352390da89ca7b/>
</Center>
</Box>
  <Box>
  <HStack>
  <Button_05b70e762d6a808a6ceb837a1ccd10c3/>
  <Button_8124dab5d6f22fa178e62c1544fe6d26/>
  <Button_1dd91b1a1af538459f585273b2710bef/>
  <Button_258adb2cf5ba98bbc099f86f06b59840/>
  <Button_3817651f523055b741ad9e694f2fa789/>
</HStack>
</Box>
</VStack>
  <VStack>
  <Heading sx={{"fontSize": "1.4em", "color": "#FFFFFF"}}>
  {`El Primero De 3 Gana`}
</Heading>
  <Heading sx={{"fontSize": "2.7em", "color": "#FFFFFF"}}>
  {`|`}
</Heading>
  <Heading sx={{"fontSize": "2.7em", "color": "#FFFFFF"}}>
  {`|`}
</Heading>
  <Heading sx={{"fontSize": "2.7em", "color": "#FFFFFF"}}>
  {`|`}
</Heading>
  <Heading sx={{"fontSize": "2.7em", "color": "#FFFFFF"}}>
  {`|`}
</Heading>
  <Heading sx={{"fontSize": "2.7em", "color": "#FFFFFF"}}>
  {`|`}
</Heading>
  <Heading sx={{"fontSize": "2.7em", "color": "#FFFFFF"}}>
  {`|`}
</Heading>
</VStack>
  <VStack>
  <Text sx={{"fontSize": "1.4em"}}>
  <Text as={`span`} sx={{"color": "#FFFFFF"}}>
  {`puntuación : `}
</Text>
  <Text_de4a4940a1e23bbc02e87e1cb88e4fa5/>
</Text>
  <Box sx={{"borderRadius": "0.9em", "background": "#FF5C00", "marginX": "1.5em", "marginY": "1em", "padding": "0.8", "border": "1px solid #000", "boxShadow": "2px 2px 2px 0px #32135A", "width": "100%"}}>
  <Center>
  <Heading_6429a6a857b9b703b639ec0ba51dc3d2/>
</Center>
</Box>
  <Button sx={{"borderRadius": "10em", "background": "#32135A", "border": "1px solid #000", "boxShadow": "2px 2x 2px 0px #FF5C00"}}>
  {`###N . P . C###`}
</Button>
</VStack>
</HStack>
</Center>
</Box>
  <NextHead>
  <title>
  {`Reflex App`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
