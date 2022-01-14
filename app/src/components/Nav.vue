<template>
	<nav>
		<button class="navTogglerButton" type="button">
			<span class="navToggler"></span>
		</button>
		<ul class="navbar-nav">
			<li class="nav-item" :class="{'color-nav': $route.path == '/'}">
				<router-link class="nav-link" to="/">Home</router-link>
			</li>
			<li class="nav-item" :class="{'color-nav': $route.path.includes('/blog')}">
				<router-link class="nav-link" to="/blog">Blog</router-link>
			</li>
			<li class="nav-item" :class="{'color-nav': $route.path.includes('/playground')}">
				<router-link class="nav-link" to="/playground">Playground</router-link>
			</li>
			<li class="nav-item" :class="{'color-nav': $route.path == '/contact'}">
				<router-link class="nav-link" to="/contact">Contact</router-link>
			</li>
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
	}
}
</script>

<style scoped>
nav {
	margin: 5px 0;
}
.navToggler {
	background-image: url("../util/img/hamburger.svg")
}
.active {
	background: darksalmon
}
@media (min-width: 992px) {
}

@media (min-width: 992px) {
	.nav-link {
		padding: 10px 20px;
	}

	.navbar-nav {
		flex-grow: 1;
		justify-content: center;
		display: flex;
	}

	.navTogglerButton {
		display: none;
	}


}

.nav-item {
	transition: all 0.5s ease;
	font-size: 1.5rem;
	list-style: none;
	padding: 10px 0;
}
.nav-link:focus {
	color:black;
}
.nav-link {
		text-decoration: none;
    color: black;
}
.nav-link:hover {
	color: white;
	transition-property: color;
	transition-duration: 0.5s;
	transition-timing-function: ease-out;
}

@media (min-width: 992px) {
	.color-nav {
		background: darksalmon;
	}
	.nav-item:hover {
		background:darksalmon;
	}
}
</style>