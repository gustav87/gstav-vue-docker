<template>
	<nav class="navbar navbar-expand-lg navbar-light">
		<div class="container-fluid">
			<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
				<span class="navbar-toggler-icon"></span>
			</button>
			<div class="collapse navbar-collapse" id="navbarSupportedContent">
				<ul class="navbar-nav me-auto mb-2 mb-lg-0">
					<li class="nav-item" :class="{'color-nav': $route.path == '/'}">
						<router-link class="nav-link" to="/">Home</router-link>
					</li>
					<li class="nav-item" :class="{'color-nav': $route.path == '/blog'}">
						<router-link class="nav-link" to="/blog">Blog</router-link>
					</li>
					<li class="nav-item" :class="{'color-nav': $route.path == '/playground'}">
						<router-link class="nav-link" to="/playground">Playground</router-link>
					</li>
					<li class="nav-item" :class="{'color-nav': $route.path == '/contact'}">
						<router-link class="nav-link" to="/contact">Contact</router-link>
					</li>
				</ul>
			</div>
		</div>
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
.active {
	background: darksalmon
}
@media (min-width: 992px) {
	.navbar-expand-lg .navbar-nav {
			flex-grow: 1;
			justify-content: center;
	}
}

@media (min-width: 992px) {
	.navbar-expand-lg .navbar-nav .nav-link {
		padding-right: 20px;
		padding-left: 20px;
	}
}

.nav-item {
	transition: all 0.5s ease;
	font-size: 1.5rem;
}
.nav-item:hover {
	background:darksalmon;
}
.navbar-light .navbar-nav .nav-link:focus {
	color:black;
}
.navbar-light .navbar-nav .nav-link {
    color: black;
}
.navbar-light .navbar-nav .nav-link:hover {
	color: white;
	transition-property: color;
	transition-duration: 0.5s;
	transition-timing-function: ease-out;
}

.color-nav {
	background: darksalmon;
}
</style>