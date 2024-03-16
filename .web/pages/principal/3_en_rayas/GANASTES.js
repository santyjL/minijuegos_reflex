/** @jsxImportSource @emotion/react */


import { Fragment } from "react"
import { Button_1e8c0375e28b2af9d011a4a0800c839a, Button_e96e0d64028ed5af77bcf3233f56d843, Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Box, Center, HStack, Text, VStack } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import NextHead from "next/head"



export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <Box sx={{"bg": "#292833", "backgroundSize": "cover", "top": 0, "width": "100%", "height": "100vh"}}>
  <Center>
  <VStack>
  <Text sx={{"fontSize": "13.5em", "color": "#FFFFFF"}}>
  {`HAS GANADO`}
</Text>
  <HStack>
  <Button_1e8c0375e28b2af9d011a4a0800c839a/>
  <Button_e96e0d64028ed5af77bcf3233f56d843/>
</HStack>
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
