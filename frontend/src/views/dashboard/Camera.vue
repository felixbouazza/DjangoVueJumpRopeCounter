<template>
  <div>
    <img>
    <button id="save">Save</button>
  </div>
</template>

<script>
const P5 = require('p5');
import axios from "axios";

export default {
  name: 'App',
  mounted() {   
    const script = function (p5) {    
      
      let video;
      let img = document.getElementsByTagName("img")
      let save = document.getElementById("save")

      // Configuration
      p5.setup = () => {    
        // p5.noCanvas()
        video = p5.createCapture(p5.VIDEO)
        // video.hide()

        save.addEventListener("click", () => {
          video.loadPixels()
          let data = {
              "image": video.canvas.toDataURL()
          }
          axios.post("/api/v1/send_frame/", data)
              .then(response => {
                  console.log(response.data.neckPoint)
              })
              .catch(error => {
                  console.log(error)
              })
          })
      }

      // For each frame
      // p5.draw = () => {
      //   video.loadPixels()
      //   let data = {
      //       "image": video.canvas.toDataURL()
      //   }
      //   axios.post("/api/v1/send_frame/", data)
      //       .then(response => {
      //           // img.src = response.data.image
      //           console.log(response.data.neckPoint)
      //       })
      //       .catch(error => {
      //           console.log(error)
      //       })
      // }
    }
    // Instance mode
    new P5(script)
  }
}
</script>

<style>

</style>