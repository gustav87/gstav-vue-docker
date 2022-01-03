<template>
<main class="content">
	<div class="backNavigation">
		<p><router-link to="/playground">Back to playground</router-link></p>
	</div>
	<div>
		<p>Search for a username on GitHub and display their repositories!</p>
	</div>
	<form name="searchUser" @submit="search(username)">
		<input type="search" placeholder="username to find" v-model="username" required>
		<input type="submit" value="Search">
		<p>Automatic search in {{countdown}} seconds.</p>
	</form>
</main>
</template>

<script>
export default {
  name: 'GithubSearch',
  components: {
  },
  data() {
    return {
      username: 'angular',
      countdown: 5
    }
  },
  methods: {
    search(username) {
      this.$router.push(`githubUser/${this.username}`)
    },
    startCountdown() {
      this.intervalID = setInterval(this.decrementCountdown, 1000);
    },
    decrementCountdown() {
      this.countdown -= 1;
      this.checkCountdown();
    },
    checkCountdown() {
      if (this.countdown <= 0) {
        this.search();
      }
    }
  },
  created() {
    this.startCountdown()
  },
  beforeUnmount() {
    clearInterval(this.intervalID)
  }
}
</script>

<style scoped>
</style>