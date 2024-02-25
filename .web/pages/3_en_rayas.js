/** @jsxImportSource @emotion/react */


import { Fragment } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Box, Heading, HStack, Image as ChakraImage, Link, Spacer, Stack, Text, VStack } from "@chakra-ui/react"
import NextLink from "next/link"
import "focus-visible/dist/focus-visible"
import NextHead from "next/head"



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
  {`-Tu-`}
</Heading>
  <Heading size={`xl`} sx={{"color": "#000000"}}>
  {`Puntaje: `}
</Heading>
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
  <Heading size={`xl`} sx={{"color": "#000000"}}>
  {`Puntaje: `}
</Heading>
</VStack>
</HStack>
</Box>
</VStack>
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
