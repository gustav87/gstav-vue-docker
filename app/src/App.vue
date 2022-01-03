<template>
  <div class="pageWrapper">
    <header>
        <h1><a href='/'>Gustav Andersson</a></h1>
		</header>
    <div class="bigWrapper">
			<Nav/>
			<router-view></router-view>
    	<footer>Gustav Andersson 2016</footer>
		</div>
  </div>
</template>

<script>
import Nav from './components/Nav.vue'

export default {
  name: 'App',
  components: {
    Nav
  },
  data() {
    return {
      showAddTask: false
    }
  },
  mounted() {
    let mapScript = document.createElement('script')
    mapScript.async = true
    mapScript.defer = true
    mapScript.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyDArSXIEl4x-YPh7iu_enHlm1AnPWyqGU4'
    document.head.appendChild(mapScript)
  },
  methods: {
    toggleAddTask() {
      this.showAddTask = !this.showAddTask
    }
  }
}
</script>

<style>
::selection {background: #54aa47;}
html, body, main, header, nav, footer, ul, ol, div, h1, h2, h3, h4, h5, h6 {margin: 0; padding:0;}
h1, h2, h3, h4, h5, h6 {font-family: 'Alex Brush', Helvetica, sans-serif; font-weight: 400;}
body {
	font-family: 'Roboto', sans-serif;
	background: linear-gradient(290deg, rgba(148,187,233,0.8813726174063375) 11%, rgba(174,238,181,0.9009804605435925) 100%);
/*	background: linear-gradient(90deg, #DAD299 10%, #B0DAB9 90%); OR linear-gradient(0deg, #61677B, #CA728F);
	background: linear-gradient(60deg, #DAD299, #B0DAB9);*/
	min-width: 320px; }
footer {
	display: flex;
	flex-direction: column;
	justify-content: center;
	background-color: gray;
  opacity: 0.8;
	text-align: center;
	height: 30px;
	width: 100%;
	position: fixed;
	bottom: 0;}
header {
	height: 65px;
	border-bottom: 2px solid black;
	text-align:center;
	box-sizing: border-box;
	cursor: default;}
header h1 {
	font-size: 2.9em;
	padding-top: 5px;}
header h1 a {
	text-decoration: none;
	color: black;
}
header span {
	font-family: 'Roboto';
	font-size: 0.36em;
	display: none;}

main h2 {font-size: 2.15em;}
main p {font-size: 1.1em;}

#blogPage, #playgroundPage {
	display: flex;

}
p {
	margin-top: 0;
}
ul, li {
	list-style: none;
}

.active {background: darksalmon}

main {
  max-width: 1000px;
	min-height: 200px;
	clear: both;
	border: 2px solid darksalmon;
	padding: 5px;
	margin: 10px auto 40px;
}

@media (min-width: 1020px) {
	header {
		height: 120px;
	}
	header h1 {
		font-size: 6em;
	}
}
@media (min-width: 620px) {
	header span {
		display: inline;
	}
}
@media (min-width: 500px) {
	main p {
		font-size: 1.2em;
	}
	main h2 {
		font-size: 3em;
	}
}

/*blueTable design start*/
.blueTable {border-collapse: collapse; width: 50%; margin-top:15px;}
.blueTable .firstRow td {padding-top: 15px;}
.blueTable td {padding: 8px; border: 1px solid blue; vertical-align: top;}
.stars {
	text-align: center;
}
/*blueTable design end*/

.box {
	padding: 10px;
  margin: 5px;
	border: 2px solid #54aa47;
	border-radius: 10px;
}
</style>
