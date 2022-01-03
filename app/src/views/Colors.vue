<template>
  <main>
    <div class="flexContainer">
      <div class="flexitem currentcolor" id="currentRed" :style="redStyle">{{this.redColor}}</div>
      <div class="flexitem currentcolor" id="currentGreen" :style="greenStyle">{{this.greenColor}}</div>
      <div class="flexitem currentcolor" id="currentBlue" :style="blueStyle">{{this.blueColor}}</div>
    </div>
    <div class="flexContainer">
      <div class="flexitem colorBoxes" id="red" @mouseleave="stopInterval()" @mouseenter="startInterval('redColor', true)">Increase red</div>
      <div class="flexitem colorBoxes" id="green" @mouseleave="stopInterval()" @mouseenter="startInterval('greenColor', true)">Increase green</div>
      <div class="flexitem colorBoxes" id="blue" @mouseleave="stopInterval()" @mouseenter="startInterval('blueColor', true)">Increase blue</div>
    </div>
    <div class="flexContainer">
      <div class="flexitem whiteBoxes" @mouseleave="stopInterval()" @mouseenter="startInterval('redColor', false)">Decrease red</div>
      <div class="flexitem whiteBoxes" @mouseleave="stopInterval()" @mouseenter="startInterval('greenColor', false)">Decrease green</div>
      <div class="flexitem whiteBoxes" @mouseleave="stopInterval()" @mouseenter="startInterval('blueColor', false)">Decrease blue</div>
    </div>
    <div class="flexContainer">
      <div class="flexitem colorBucket" :style="bucketStyle">
        <span>Color bucket</span>
        <span>Color bucket</span>
        <span>Color bucket</span>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  name: 'Colors',
  components: {
  },
  data() {
    return {
      redColor: 0,
      greenColor: 0,
      blueColor: 0,
      redStyle: {background: "rgb(0,0,0)"},
      greenStyle: {background: "rgb(0,0,0)"},
      blueStyle: {background: "rgb(0,0,0)"},
      bucketStyle: {
        background: "rgb(0,0,0)",
        color: 255
      },
      bucketColor: 255,
      intervalID: null
    }
  },
  methods: {
    startInterval(color, increase) {
      this.intervalID = setInterval(this.changeColor, 10, color, increase)
    },
    changeColor(color, increase) {
      if ((increase && this[color] >= 255) || (!increase && this[color] <= 0)) {
        return
      }
      const increment = increase ? 1 : -1
      this[color] = this[color] + increment
      if (color == "redColor") {
        this.redStyle = {
          background: "rgb(" + this[color] + ",0,0)"
        }
      } else if (color == "greenColor") {
        this.greenStyle = {
          background: "rgb(0," + this[color] + ",0)"
        }
      } else {
        this.blueStyle = {
          background: "rgb(0,0," + this[color] + ")"
        }
      }
      this.bucketColor = Math.floor(255 - ((this.redColor + this.greenColor + this.blueColor) / 3))
      this.bucketStyle = {
        background: "rgb(" + this.redColor + "," + this.greenColor + "," + this.blueColor + ")",
        color: "rgb(" + this.bucketColor + "," + this.bucketColor + "," + this.bucketColor + ")"
      }
    },
    stopInterval() {
      clearInterval(this.intervalID)
    }
  }
}
</script>

<style scoped>
main {color: white;}
main .whiteBoxes {color: black;}
main > div {
	display: flex;
	justify-content: stretch;
}
.colorBucket {
	display: flex;
	justify-content: space-around;
}
.flexitem {
	width: 100%;
	padding: 10px;
	margin: 10px;
}

.whiteBoxes {background: white;}
#red {background: red;}
#green {background: green;}
#blue {background: blue;}
</style>