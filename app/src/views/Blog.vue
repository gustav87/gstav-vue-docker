<template>
  <main id="blogPage">
    <SideNav :sideNavItems="sideNavItems" />
    <div class="display box"><p>Blogpage</p></div>
  </main>
</template>

<script>
import SideNav from '../components/SideNav.vue'

export default {
  name: 'Blog',
  props: {},
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
      {text: "Blogpost 1", url: "notyet"},
      {text: "Blogpost 2", url: "notyet"},
      {text: "Blogpost 3", url: "notyet"},
      {text: "Blogpost 4", url: "notyet"}
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