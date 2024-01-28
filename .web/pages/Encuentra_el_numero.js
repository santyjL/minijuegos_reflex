/** @jsxImportSource @emotion/react */


import { Fragment } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0, Text_ca96b91b89c4e309931e832638edcbcf } from "/utils/stateful_components"
import { Box, Center, Heading, HStack, Image as ChakraImage, Link, Spacer, Text, VStack } from "@chakra-ui/react"
import NextLink from "next/link"
import "focus-visible/dist/focus-visible"
import NextHead from "next/head"



export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <Box sx={{"bg": "#292833", "backgroundSize": "cover", "width": "100%", "height": "100vh"}}>
  <Box sx={{"bg": "#FF5C00", "border": "1px solid #000"}}>
  <HStack>
  <Link as={NextLink} href={`principal`}>
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
  <Link as={NextLink} href={`https://github.com/santyjL/santyjL`} isExternal={true}>
  <ChakraImage src={`/github icon.png`} sx={{"width": "3.6em", "height": "100%"}}/>
</Link>
</HStack>
</Box>
  <Center>
  <VStack>
  <Box sx={{"borderRadius": "0.9em", "background": "#32135A", "marginX": "1.5em", "marginY": "1em", "padding": "0.8", "border": "1px solid #000", "boxShadow": "1px 1px 1px 0px #FF5C00", "width": "70%", "margin": "3em"}}>
  <Center>
  <HStack sx={{"marginX": "1.5em", "marginY": "1em"}}>
  <Text sx={{"color": "#C1C1C1", "fontSize": "1.4em"}}>
  {`Encuentra el numero , tenes 5 oportunidades para encontrar el numero , si lo logras habras ganado y si no habras perdido suerte`}
</Text>
</HStack>
</Center>
</Box>
  <Center sx={{"width": "100%"}}>
  <HStack>
  <Box sx={{"borderRadius": "0.9em", "background": "#32135A", "marginX": "1.5em", "marginY": "1em", "padding": "0.8", "border": "1px solid #000", "boxShadow": "1px 1px 1px 0px #FF5C00", "width": "50%", "textAlig": "left"}}>
  <HStack>
  <Text_ca96b91b89c4e309931e832638edcbcf/>
</HStack>
</Box>
  <Spacer/>
  <Box sx={{"borderRadius": "0.9em", "background": "#32135A", "marginX": "1.5em", "marginY": "1em", "padding": "0.8", "border": "1px solid #000", "boxShadow": "1px 1px 1px 0px #FF5C00", "width": "50%"}}>
  <HStack>
  <Text_ca96b91b89c4e309931e832638edcbcf/>
</HStack>
</Box>
</HStack>
</Center>
</VStack>
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
