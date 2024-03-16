/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Box, Button, Center, Grid, GridItem, Heading, HStack, Image as ChakraImage, Link, Spacer, Stack, Text, VStack } from "@chakra-ui/react"
import NextLink from "next/link"
import "@radix-ui/themes/styles.css"
import "focus-visible/dist/focus-visible"
import { EventLoopContext, StateContexts } from "/utils/context"
import { Theme as RadixThemesTheme } from "@radix-ui/themes"
import range from "/utils/helpers/range.js"
import { Event, isTrue } from "/utils/state"
import NextHead from "next/head"



export function Heading_adfb67a61fb354e94360d31f89a46edf () {
  const state__tic_tac_toe_state = useContext(StateContexts.state__tic_tac_toe_state)


  return (
    <Heading size={`xl`} sx={{"color": "#000000"}}>
  {`Puntaje:${state__tic_tac_toe_state.puntuacion_npc}`}
</Heading>
  )
}

export function Heading_621d22890f19e824cb64257d0d9a5049 () {
  const state__tic_tac_toe_state = useContext(StateContexts.state__tic_tac_toe_state)


  return (
    <Heading size={`xl`} sx={{"color": "#000000"}}>
  {`Puntaje:${state__tic_tac_toe_state.puntuacion_jugador}`}
</Heading>
  )
}

export function Grid_d3e73f0629b3b0adb840a442d95ec883 () {
  const state__tic_tac_toe_state = useContext(StateContexts.state__tic_tac_toe_state)
  const [addEvents, connectError] = useContext(EventLoopContext);


  return (
    <Grid sx={{"gap": 4}} templateColumns={`repeat(3, 1fr)`} templateRows={`repeat(3, 1fr)`}>
  {Array.from(range(3, undefined, 1)).map((x, index_8e9528d12c07c54f1890c7b2255aae6c) => (
  <Fragment key={index_8e9528d12c07c54f1890c7b2255aae6c}>
  {Array.from(range(3, undefined, 1)).map((y, index_56c7a86aac840fc84d1be1e7446a9d47) => (
  <GridItem colSpan={1} key={index_56c7a86aac840fc84d1be1e7446a9d47} rowSpan={1}>
  <Fragment>
  {isTrue((state__tic_tac_toe_state.matriz.at(x).at(y) === "")) ? (
  <Fragment>
  <Button onClick={(_e) => addEvents([Event("state.tic_tac_toe_state.juego", {x:x,y:y})], (_e), {})} sx={{"padding": 10}}>
  <Text sx={{"fontSize": "2.7em"}}>
  {`⬜`}
</Text>
</Button>
</Fragment>
) : (
  <Fragment>
  <Button sx={{"disabled": true, "padding": 10}}>
  <Text sx={{"fontSize": "2.7em"}}>
  {state__tic_tac_toe_state.matriz.at(x).at(y)}
</Text>
</Button>
</Fragment>
)}
</Fragment>
</GridItem>
))}
</Fragment>
))}
</Grid>
  )
}

export function Button_3b929957eb62487495b1f4884da434bb () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_f830e27fcc2268a80e702ba6076429be = useCallback((_e) => addEvents([Event("state.tic_tac_toe_state.reiniciar_juego", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_f830e27fcc2268a80e702ba6076429be} sx={{"borderRadius": "0.9em", "background": "#32135A", "border": "1px solid #000", "boxShadow": "2px 2x 2px 0px #FF5C00"}}>
  {`Reset`}
</Button>
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
  <VStack>
  <Box sx={{"marginX": "1.5em", "marginY": "1em"}}>
  <HStack spacing={`16em`}>
  <VStack>
  <Heading size={`2xl`} sx={{"color": "#000000"}}>
  {`-NPC-`}
</Heading>
  <Heading_adfb67a61fb354e94360d31f89a46edf/>
</VStack>
  <Stack sx={{"borderRadius": "0.9em", "background": "#32135A", "marginX": "1.5em", "marginY": "1em", "padding": "0.8", "border": "1px solid #000", "boxShadow": "2px 2px 2px 0px #FF5C00", "width": "100%", "margin": "3em"}}>
  <Text sx={{"color": "#FFFFFF", "fontSize": "2.7em"}}>
  {`El primero de 5 gana`}
</Text>
</Stack>
  <VStack>
  <Heading size={`2xl`} sx={{"color": "#000000"}}>
  {`-Tu-`}
</Heading>
  <Heading_621d22890f19e824cb64257d0d9a5049/>
</VStack>
</HStack>
</Box>
</VStack>
  <Center>
  <HStack sx={{"boxShadow": "11px 11px 11px 0px #FF5C00 , -11px -11px 11px 0px #32135A", "padding": 10}}>
  <Grid_d3e73f0629b3b0adb840a442d95ec883/>
</HStack>
</Center>
  <Center sx={{"margin": "1em"}}>
  <Button_3b929957eb62487495b1f4884da434bb/>
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
