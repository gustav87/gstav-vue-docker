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
	width: 350px;
  font-size: 1.4rem;
}

a {
  text-decoration: none;
  color: black;
}

a:hover {
  color: #0a58ca;
}

ul {
  /* margin-top: 0.5rem;
  margin-bottom: 0.5rem; */
  padding: 0.5rem 0;
  padding-left: 1rem;
  margin: 0;
}

li {
	list-style: none;
}
</style>
