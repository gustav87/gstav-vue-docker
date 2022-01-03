<template>
  <main class="content">
    <p>Input anything into the Name and Email fields to insert a record into the database.</p>
    <form id="insertRowForm" @submit.prevent="submitInsertRowForm">
      <label for="name" id="nameLabel">Name:</label>
      <input type="text" name="name" id="name" v-model="name">
      <label for="email">Email: </label>
      <input type="text" name="email" id="email" v-model="email">
      <input type="submit" value="send">
    </form>
    <p id="insertRowResult"></p>
    <hr>
    <p>Search the database. You can filter by name.</p>
    <form id="searchDbForm" @submit.prevent="submitSearchDbForm">
      <label for="filter">Filter by name: </label>
      <input type="text" name="filter" id="filter" v-model="filter">
      <input type="submit" value="Search database">
    </form>
    <table v-if="showTable" id="getAllDocsResult">
      <tr>
        <th>Name</th>
        <th>Email</th>
        <th>Date added</th>
      </tr>
      <tr v-for="document in documents">
        <td>{{document.name}}</td>
        <td>{{document.email}}</td>
        <td>{{document.dateAdded}}</td>
      </tr>
    </table>
  </main>
</template>

<script>
export default {
  name: 'DbStuff',
  props: {},
  components: {
  },
  data() {
    return {
      name: null,
      email: null,
      filter: null,
      showTable: false,
      documents: {}
    }
  },
  methods: {
    async submitInsertRowForm() {
      const location = window.location.hostname
      const requestOptions = {
        method: 'POST',
        headers: {Accept: 'application/json', 'Content-Type': 'application/json'},
        body: JSON.stringify({name: this.name, email: this.email})
      }
      try {
        fetch(`http://${location}:5000/backend/databasics/insertRow`, requestOptions)
          .then(response => response.text())
          .then(res => {
            console.log(res)
          })
      } catch (err) {
        console.log(err)
      }    
    },
    submitSearchDbForm() {
      const location = window.location.hostname
      const queryString = this.filter ? `?filter=${this.filter}` : ''
      fetch(`http://${location}:5000/backend/databasics/getDocuments${queryString}`)
        .then(response => response.json())
        .then(res => {
          this.showTable = true
          this.documents = res
        })
      
    }
  }
}
</script>

<style scoped>
input {
  display: block;
  margin-bottom: 5px;
}

th {
  text-align: left;
}

hr {
  border-top: 1px solid black;
}

#filter {
  display: inline;
}
</style>