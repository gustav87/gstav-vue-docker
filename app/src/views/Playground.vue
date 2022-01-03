<template>
  <main id="playgroundPage">
    <SideNav :sideNavItems="sideNavItems"/>
    <div class="display box"><p>Playgroundpage</p></div>
  </main>
</template>

<script>
import SideNav from '../components/SideNav.vue'

export default {
  name: 'Playground',
  components: {
    SideNav
  },
  data() {
    return {
      sideNavItems: []
    }
  },
  created() {
    this.sideNavItems = [
      {
        "url": "/playground/githubSearch",
        "text": "Github viewer"
      },
      {
        "url": "/playground/colors",
        "text": "Playing with colors"
      },
      {
        "url": "/playground/map",
        "text": "Map"
      },
      {
        "url": "/playground/flickrViewer",
        "text": "Flickr viewer"
      },
      {
        "url": "/playground/dbStuff",
        "text": "Database stuff"
      }
      // {
      //   "url": "/playground/vueStuff",
      //   "text": "Vue stuff"
      // },
      // {
      //   "url": "/playground/jsStuff",
      //   "text": "JavaScript stuff"
      // }
    ]
  }
}
</script>

<style scoped>
.display {
	width: 100%;
	margin-left: 10px;
}
</style>