<template>
  <main class="content">
    <div class="flexContainer">
      <div class="backButtons">
        <p><router-link to="/playground">Back to playground</router-link></p>
        <p><router-link to="/playground/githubSearch">Back to search</router-link></p>
      </div>
      <div class="githubInfo">
        <div>Choose sort order:</div>
        <select v-model="repoSortOrder" name="fishy">
          <option value="+stargazers_count">Stars, ascending</option>
          <option value="-stargazers_count">Stars, descending</option>
          <option value="+name">Name, ascending</option>
          <option value="-name">Name, descending</option>
          <option value="+language">Language, ascending</option>
          <option value="-language">Language, descending</option>
        </select>
        <div><img id="img1" :src="account.avatar_url" :title="account.name"></div>
        <p>You searched for: {{username}}</p>
        <div id="userDetails">Username: {{account.name}}</div>
        <div>User location: {{account.location}}</div>	
      </div>
      <div class="githubTable">
        <table class="blueTable">
          <thead><tr><th>Name</th><th>Stars</th><th>Language</th></tr></thead>
          <tbody v-for="item in sortedRepos">
            <tr>
              <td>{{item.name}}</td>
              <td class="stars">
                {{item.stargazers_count}} 
                <i class="fa fa-star-o fa-lg" aria-hidden="true"></i>
              </td>
              <td>{{item.language}}</td>
            </tr>
          </tbody>
        </table>	
      </div>
    </div>
  </main>
</template>

<script>
export default {
  name: 'GithubUser',
  components: {
  },
  data() {
    return {
      username: this.$route.params.username,
      account: {},
      repoSortOrder: '+stargazers_count',
      repos: []
    }
  },
  methods: {
    async searchUser() {
      console.log("searching!")
    }
  },
  async created() {
    // this.account = this.searchUser()
    this.account = await fetch(`https://api.github.com/users/${this.username}`)
      .then(response => response.json())
    this.repos = await fetch(this.account.repos_url)
      .then(response => response.json())
  },
  computed: {
    // sortedRepos: function() {
    //   return this.repos.sort((a, b) => b.stargazers_count - a.stargazers_count)
    // }
    sortedRepos: function() {
      switch(this.repoSortOrder) {
        case '+stargazers_count':
          return this.repos.sort((a, b) => a.stargazers_count - b.stargazers_count)
        case '-stargazers_count':
          return this.repos.sort((a, b) => b.stargazers_count - a.stargazers_count)
        case '+name':
          return this.repos.sort((a, b) => a.name < b.name ? -1 : 1)
        case '-name':
          return this.repos.sort((a, b) => b.name < a.name ? -1 : 1)
        case '+language':
          return this.repos.sort((a, b) => a.language < b.language ? -1 : 1)
        case '-language':
          return this.repos.sort((a, b) => b.language < a.language ? -1 : 1)
      }
    }
  }
}
</script>

<style scoped>
.flexContainer {
	display: flex;
	justify-content: space-between;
}

img {width: 200px;}
</style>