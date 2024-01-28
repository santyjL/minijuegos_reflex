/** @jsxImportSource @emotion/react */


import { Fragment } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Box, Button, Center, Heading, HStack, Image as ChakraImage, Link, Spacer, Text, VStack } from "@chakra-ui/react"
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
  <Box sx={{"width": "100%"}}>
  <Center sx={{"borderRadius": "0.9em", "background": "#32135A", "marginX": "1.5em", "marginY": "1em", "padding": "0.8", "border": "1px solid #000", "boxShadow": "1px 1px 1px 0px #FF5C00", "width": null}}>
  <VStack>
  <HStack>
  <Heading sx={{"color": "#FFFFFF", "fontSize": "2.7em"}}>
  {`Piedra🥌 , Papel📋 , Tijeras✂ , Lagarto🦎 , Spock 🖖`}
</Heading>
</HStack>
  <HStack>
  <Box sx={{"textAlign": "left"}}>
  <HStack>
  <Text sx={{"color": "#FFFFFF", "fontSize": "1.4em"}}>
  {`1.Piedra aplasta Tijeras : `}
</Text>
  <Text sx={{"color": "#C1C1C1", "fontSize": "1.4em"}}>
  {`La Piedra gana porque puede romper las Tijeras.`}
</Text>
</HStack>
  <HStack>
  <Text sx={{"color": "#FFFFFF", "fontSize": "1.4em"}}>
  {`2.Tijeras cortan Papel : `}
</Text>
  <Text sx={{"color": "#C1C1C1", "fontSize": "1.4em"}}>
  {`Las Tijeras ganan al cortar el Papel.`}
</Text>
</HStack>
  <HStack>
  <Text sx={{"color": "#FFFFFF", "fontSize": "1.4em"}}>
  {`3.Papel cubre Piedra : `}
</Text>
  <Text sx={{"color": "#C1C1C1", "fontSize": "1.4em"}}>
  {`El Papel gana al cubrir la Piedra. `}
</Text>
</HStack>
  <HStack>
  <Text sx={{"color": "#FFFFFF", "fontSize": "1.4em"}}>
  {`4.Piedra aplasta Lagarto : `}
</Text>
  <Text sx={{"color": "#C1C1C1", "fontSize": "1.4em"}}>
  {`La Piedra gana al aplastar al Lagarto.`}
</Text>
</HStack>
  <HStack>
  <Text sx={{"color": "#FFFFFF", "fontSize": "1.4em"}}>
  {`5.Lagarto envenena Spock :  `}
</Text>
  <Text sx={{"color": "#C1C1C1", "fontSize": "1.4em"}}>
  {`El Lagarto gana al envenenar a Spock.`}
</Text>
</HStack>
  <HStack>
  <Text sx={{"color": "#FFFFFF", "fontSize": "1.4em"}}>
  {`6.Spock destroza Tijeras:`}
</Text>
  <Text sx={{"color": "#C1C1C1", "fontSize": "1.4em"}}>
  {`Spock gana al destrozar las Tijeras.`}
</Text>
</HStack>
  <HStack>
  <Text sx={{"color": "#FFFFFF", "fontSize": "1.4em"}}>
  {`7.Tijeras decapitan Lagarto : `}
</Text>
  <Text sx={{"color": "#C1C1C1", "fontSize": "1.4em"}}>
  {`Las Tijeras ganan al decapitar al Lagarto.`}
</Text>
</HStack>
  <HStack>
  <Text sx={{"color": "#FFFFFF", "fontSize": "1.4em"}}>
  {`8.Lagarto come Papel : `}
</Text>
  <Text sx={{"color": "#C1C1C1", "fontSize": "1.4em"}}>
  {`El Lagarto gana al comer el Papel.`}
</Text>
</HStack>
  <HStack>
  <Text sx={{"color": "#FFFFFF", "fontSize": "1.4em"}}>
  {`9.Papel desautoriza Spock : `}
</Text>
  <Text sx={{"color": "#C1C1C1", "fontSize": "1.4em"}}>
  {`El Papel gana al desautorizar a Spock.`}
</Text>
</HStack>
  <HStack>
  <Text sx={{"color": "#FFFFFF", "fontSize": "1.4em"}}>
  {`10.Spock vaporiza Piedra:`}
</Text>
  <Text sx={{"color": "#C1C1C1", "fontSize": "1.4em"}}>
  {`Spock gana al vaporizar la Piedra.`}
</Text>
</HStack>
</Box>
</HStack>
</VStack>
</Center>
</Box>
  <Button sx={{"borderRadius": "0.9em", "background": "#FF5C00", "border": "1px solid #000", "boxShadow": "1px 1px 1px 0px #32135A", "marginLeft": "75%"}}>
  <Link as={NextLink} href={`3_en_rayas`}>
  <Text sx={{"fontSize": "2.7em"}}>
  {`continuar`}
</Text>
</Link>
</Button>
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
