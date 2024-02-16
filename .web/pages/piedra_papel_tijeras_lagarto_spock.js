/** @jsxImportSource @emotion/react */


import { Fragment, useContext } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Box, Center, Heading, HStack, Image as ChakraImage, Link, Spacer, VStack } from "@chakra-ui/react"
import NextLink from "next/link"
import "focus-visible/dist/focus-visible"
import { StateContexts } from "/utils/context"
import NextHead from "next/head"



export function Heading_d2c3016c1744cec37ad9aa47d0e64cf0 () {
  const state__estados = useContext(StateContexts.state__estados)


  return (
    <Heading sx={{"fontSize": "13.5em", "padding": 20}}>
  {state__estados.jugadas_npc}
</Heading>
  )
}

export function Heading_d8fb636aa9d95536b22ebf8241e93734 () {
  const state__estados = useContext(StateContexts.state__estados)


  return (
    <Heading sx={{"fontSize": "13.5em", "padding": 20}}>
  {state__estados.jugadas_jugador}
</Heading>
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
  <Box sx={{"borderRadius": "0.9em", "background": "#FF5C00", "marginX": "1.5em", "marginY": "1em", "padding": "0.8", "border": "1px solid #000", "boxShadow": "2px 2px 2px 0px #32135A", "width": "29%"}}>
  <Center>
  <Heading_d8fb636aa9d95536b22ebf8241e93734/>
</Center>
</Box>
  <VStack>
  <Heading sx={{"fontSize": "1.4em"}}>
  {`El primero de 3 gana`}
</Heading>
  <Heading sx={{"fontSize": "2.7em"}}>
  {`|`}
</Heading>
  <Heading sx={{"fontSize": "2.7em"}}>
  {`|`}
</Heading>
  <Heading sx={{"fontSize": "2.7em"}}>
  {`|`}
</Heading>
  <Heading sx={{"fontSize": "2.7em"}}>
  {`|`}
</Heading>
  <Heading sx={{"fontSize": "2.7em"}}>
  {`|`}
</Heading>
  <Heading sx={{"fontSize": "2.7em"}}>
  {`|`}
</Heading>
</VStack>
  <Box sx={{"borderRadius": "0.9em", "background": "#FF5C00", "marginX": "1.5em", "marginY": "1em", "padding": "0.8", "border": "1px solid #000", "boxShadow": "2px 2px 2px 0px #32135A", "width": "29%"}}>
  <Center>
  <Heading_d2c3016c1744cec37ad9aa47d0e64cf0/>
</Center>
</Box>
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
