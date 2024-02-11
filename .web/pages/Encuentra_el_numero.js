/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Box, Button, Center, Heading, HStack, Image as ChakraImage, Link, Spacer, Text, VStack } from "@chakra-ui/react"
import NextLink from "next/link"
import "focus-visible/dist/focus-visible"
import { EventLoopContext, StateContexts } from "/utils/context"
import { Event, isTrue } from "/utils/state"
import NextHead from "next/head"



export function Fragment_f7ea8225d31638c9eab90aa15eb5499a () {
  const state__count = useContext(StateContexts.state__count)


  return (
    <Fragment>
  {isTrue((state__count.estado !== "===")) ? (
  <Fragment>
  <Button sx={{"borderRadius": "0.9em", "background": "#32135A", "border": "1px solid #000", "boxShadow": "2px 2x 2px 0px #FF5C00", "width": "100%"}}>
  <Text sx={{"fontSize": "2.7em", "color": "#FFFFFF"}}>
  {`no es igual`}
</Text>
</Button>
</Fragment>
) : (
  <Fragment>
  <Button sx={{"borderRadius": "0.9em", "background": "#32135A", "border": "1px solid #000", "boxShadow": "2px 2x 2px 0px #FF5C00", "width": "100%"}}>
  <Text sx={{"fontSize": "2.7em", "color": "#FFFFFF"}}>
  {`es igual`}
</Text>
</Button>
</Fragment>
)}
</Fragment>
  )
}

export function Button_cad2b09bade318ca06ad93c0ea2fd034 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_21645699dd924dacf2eea55657c22e10 = useCallback((_e) => addEvents([Event("state.count.decrementt_max", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_21645699dd924dacf2eea55657c22e10} sx={{"borderRadius": "0.9em", "background": "#32135A", "border": "1px solid #000", "boxShadow": "2px 2x 2px 0px #FF5C00", "width": "100%"}}>
  <Text sx={{"fontSize": "2.7em", "color": "#FFFFFF"}}>
  {`-10`}
</Text>
</Button>
  )
}

export function Button_b5086e4056c550c70f71edaee4daeb47 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_ad75cce92a4ac5120b07a0c4ee6d9fc7 = useCallback((_e) => addEvents([Event("state.count.start", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_ad75cce92a4ac5120b07a0c4ee6d9fc7} sx={{"borderRadius": "0.9em", "background": "#32135A", "border": "1px solid #000", "boxShadow": "2px 2x 2px 0px #FF5C00", "width": "100%"}}>
  <Text sx={{"fontSize": "2.7em", "color": "#FFFFFF"}}>
  {`Start`}
</Text>
</Button>
  )
}

export function Button_b4963df3f38b8fe2ecf5a66afcca8d07 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_69a557798893dbf58cd8192b8437c43d = useCallback((_e) => addEvents([Event("state.count.decrement", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_69a557798893dbf58cd8192b8437c43d} sx={{"borderRadius": "0.9em", "background": "#32135A", "border": "1px solid #000", "boxShadow": "2px 2x 2px 0px #FF5C00", "width": "100%"}}>
  <Text sx={{"fontSize": "2.7em", "color": "#FFFFFF"}}>
  {`-1`}
</Text>
</Button>
  )
}

export function Text_ca96b91b89c4e309931e832638edcbcf () {
  const state__count = useContext(StateContexts.state__count)


  return (
    <Text sx={{"fontSize": "13.5em", "color": "#000000"}}>
  {state__count.count}
</Text>
  )
}

export function Text_a818d50e4bab0d9f1ab62e77eb9eed79 () {
  const state__count = useContext(StateContexts.state__count)


  return (
    <Text sx={{"fontSize": "13.5em", "color": "#000000"}}>
  {state__count.estado}
</Text>
  )
}

export function Text_75856ce73ec21e760a94d64dc851fee1 () {
  const state__count = useContext(StateContexts.state__count)


  return (
    <Text sx={{"fontSize": "6.5em", "color": "#000000", "PADDINGX": "0.8"}}>
  {state__count.intentos}
</Text>
  )
}

export function Button_fb4a7aacd2f86980c00247a2e626ecca () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_82911dbe063caf14c99664e94196c8b5 = useCallback((_e) => addEvents([Event("state.count.increment_max", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_82911dbe063caf14c99664e94196c8b5} sx={{"borderRadius": "0.9em", "background": "#32135A", "border": "1px solid #000", "boxShadow": "2px 2x 2px 0px #FF5C00", "width": "100%"}}>
  <Text sx={{"fontSize": "2.7em", "color": "#FFFFFF"}}>
  {`+10`}
</Text>
</Button>
  )
}

export function Button_9242eb8fca959adb0b421a564330e844 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_dee734a8d69f94b42f65eab2ee1c7716 = useCallback((_e) => addEvents([Event("state.count.increment", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_dee734a8d69f94b42f65eab2ee1c7716} sx={{"borderRadius": "0.9em", "background": "#32135A", "border": "1px solid #000", "boxShadow": "2px 2x 2px 0px #FF5C00", "width": "100%"}}>
  <Text sx={{"fontSize": "2.7em", "color": "#FFFFFF"}}>
  {`+1`}
</Text>
</Button>
  )
}

export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <Box sx={{"bg": "#292833", "backgroundSize": "cover", "width": "100%", "height": "100vh"}}>
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
  <VStack>
  <Box sx={{"borderRadius": "0.9em", "background": "#32135A", "marginX": "1.5em", "marginY": "1em", "padding": "0.8", "border": "1px solid #000", "boxShadow": "2px 2px 2px 0px #FF5C00", "width": "70%", "margin": "3em"}}>
  <Center>
  <HStack sx={{"marginX": "1.5em", "marginY": "1em"}}>
  <Text sx={{"color": "#C1C1C1", "fontSize": "1.4em"}}>
  {`Encuentra el numero , tenes 5 oportunidades para encontrar el numero , si lo logras habras ganado y si no habras perdido suerte`}
</Text>
</HStack>
</Center>
</Box>
</VStack>
</Center>
  <Center>
  <HStack>
  <VStack>
  <Box sx={{"borderRadius": "0.9em", "background": "#FF5C00", "marginX": "1.5em", "marginY": "1em", "padding": "0.8", "border": "1px solid #000", "boxShadow": "2px 2px 2px 0px #32135A", "width": "100%"}}>
  <VStack>
  <HStack>
  <Text_ca96b91b89c4e309931e832638edcbcf/>
</HStack>
</VStack>
</Box>
  <Box>
  <HStack>
  <Button_fb4a7aacd2f86980c00247a2e626ecca/>
  <Button_9242eb8fca959adb0b421a564330e844/>
  <Button_b5086e4056c550c70f71edaee4daeb47/>
  <Button_cad2b09bade318ca06ad93c0ea2fd034/>
  <Button_b4963df3f38b8fe2ecf5a66afcca8d07/>
</HStack>
</Box>
</VStack>
  <Box sx={{"borderRadius": "0.9em", "background": "#FF5C00", "marginX": "1.5em", "marginY": "1em", "padding": "0.8", "border": "1px solid #000", "boxShadow": "2px 2px 2px 0px #32135A", "width": "100%"}}>
  <Center>
  <HStack>
  <Text_75856ce73ec21e760a94d64dc851fee1/>
</HStack>
</Center>
</Box>
  <VStack>
  <Box sx={{"borderRadius": "0.9em", "background": "#FF5C00", "marginX": "1.5em", "marginY": "1em", "padding": "0.8", "border": "1px solid #000", "boxShadow": "2px 2px 2px 0px #32135A", "width": "100%"}}>
  <VStack>
  <HStack>
  <Text_a818d50e4bab0d9f1ab62e77eb9eed79/>
</HStack>
</VStack>
</Box>
  <Box>
  <HStack>
  <Fragment_f7ea8225d31638c9eab90aa15eb5499a/>
</HStack>
</Box>
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
