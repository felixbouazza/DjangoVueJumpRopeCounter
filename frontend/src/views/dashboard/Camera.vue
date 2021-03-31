<template>
  <div>
    <button id="save">Prendre une photo</button>
    <img>
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
      let save = document.getElementById('save')
      let img = document.querySelector("img")
      // NOTE: Set up is here   
      p5.setup = () => {    
        p5.noCanvas()
        video = p5.createCapture(p5.VIDEO)
        video.hide()
        // save.addEventListener("click", () => {
        //     video.loadPixels()
        //     let data = {
        //         "image": video.canvas.toDataURL()
        //     }
        //     axios.post("/api/v1/send_frame/", data)
        //         .then(response => {
        //             img.src = response.data.image
        //         })
        //         .catch(error => {
        //             console.log(error)
        //         })
        //     // video.loadPixels()
        //     // let image64 = video.canvas.toDataURL()
        //     // img.src = image64
        //     // console.log("Hello world !")
        // })
      }

      p5.draw = () => {
        video.loadPixels()
          let data = {
              "image": video.canvas.toDataURL()
          }
          axios.post("/api/v1/send_frame/", data)
              .then(response => {
                  img.src = response.data.image
              })
              .catch(error => {
                  console.log(error)
              })
      }
    }    // NOTE: Use p5 as an instance mode
    new P5(script)
  }
}
</script>

<style>

</style>