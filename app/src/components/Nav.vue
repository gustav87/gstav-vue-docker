<template>
	<nav class="navbar navbar-expand-lg navbar-light">
		<div class="container-fluid">
			<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
				<span class="navbar-toggler-icon"></span>
			</button>
			<div class="collapse navbar-collapse" id="navbarSupportedContent">
				<ul class="navbar-nav me-auto mb-2 mb-lg-0">
					<li class="nav-item">
						<router-link class="nav-link" to="/">Home</router-link>
					</li>
					<li class="nav-item">
						<router-link class="nav-link" to="/blog">Blog</router-link>
					</li>
					<li class="nav-item">
						<router-link class="nav-link" to="/playground">Playground</router-link>
					</li>
					<li class="nav-item">
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

.nav-item {
	transition: all 0.5s ease;
	font-size: 1.2em;
	margin-left: 20px;
	margin-right: 20px;
}
.nav-item:hover {
	background:darksalmon;
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

/* @media (min-width: 620px) {
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
*/
</style>