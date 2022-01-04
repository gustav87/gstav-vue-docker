<template>
  <div class="box">
    <ul v-for="item in sideNavItems">
      <li><router-link :to="item.url">{{item.text}}</router-link></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'SideNav',
  props: {
    sideNavItems: Array
  }
}
</script>

<style scoped>
div {
	width: 320px;
  font-size: 1.5em;
}
div ul li {
	padding: 10px 15px;
}
</style>
