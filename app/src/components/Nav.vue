<template>
  <nav>
    <i class="fa fa-bars" @click="hello" id="menuButton" aria-hidden="true"><a href="#"></a></i>
    <ul>
      <li class="navButton"><router-link to="/">Home</router-link></li><!--
    --><li class="navButton"><router-link to="/blog">Blog</router-link></li><!--
    --><li class="navButton"><router-link to="/playground">Playground</router-link></li><!--
    --><li class="navButton"><router-link to="/contact">Contact</router-link></li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'Nav',
  props: {
    title: {
      type: String,
      default: "Hello"
    }
  },
  components: {
  },
	methods: {
		hello() {
			console.log("hey")
		}
	}
}
</script>

<style scoped>
.fa-bars {color:#54aa47;}
nav {
	width: 100%;
	border-bottom: 1px solid black;
	text-align: center;
}
nav ul {
	display: none;
	clear: both;
}
nav ul li a {
	width: 100%;
	padding: 10px 0;
	display: block;
	text-align: center;
	font-size: 1.5em;
	text-decoration: none;
	color: black;
}
#menuButton {
	display: block;
	float: right;
	font-size: 2.5em;
	margin-right: 5px;
	cursor: pointer;
}
.navButton {
	transition: all 0.5s ease;
}
.navButton:hover {
	background:darksalmon;
}
.navButton > a {
	transition-property: color;
	transition-duration: 1s;
	transition-timing-function: ease-out;
}
.navButton:hover > a {
	color: white;
}

@media (min-width: 620px) {
	#menuButton {
		display: none;
	}
	nav ul {
		display: block;
	}
	nav ul li {
		display: inline-block;
	}
	nav ul li a {
		display: inline-block;
		width: 120px;
		padding: 10px 15px;
	}
}
</style>