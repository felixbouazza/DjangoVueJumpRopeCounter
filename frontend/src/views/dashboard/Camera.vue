<template>
  <div>
    <p id="jumpCounter"></p>
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
      let jumpCounterElement = document.getElementById("jumpCounter")

      let lastSecondData = []
      let jumpCounter = 0

      // Configuration
      p5.setup = () => {    
        p5.noCanvas()
        p5.frameRate(5);
        video = p5.createCapture(p5.VIDEO)
      }

      p5.draw = () => {
        video.loadPixels()
        let data = {
            "frame": video.canvas.toDataURL(),
            "lastSecondData": lastSecondData,
            "jumpCounter": jumpCounter
        }
        axios.post("/api/v1/load_frame/", data)
            .then(response => {
                lastSecondData = response.data.lastSecondData
                jumpCounter = response.data.jumpCounter
                jumpCounterElement.innerText = jumpCounter
            })
            .catch(error => {
                console.log(error)
            })
        
      }
    }
    // Instance mode
    new P5(script)
  }
}
</script>

<style>
#jumpCounter {
  color: red;
  font-size: 80px;
}
</style>