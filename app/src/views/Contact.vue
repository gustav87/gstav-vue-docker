<template>
  <main class="content">
    <div class="box">
      <p id="header" :style="{textAlign: headerTextAlign}">{{headerText}}</p>

      <form @submit.prevent="submitForm" method="get" id="contactMeForm" :style="{display: displayForm}">
        <div>
          <label>
            <p>Name</p>
            <input type="text" v-model="name" id="name" name="name" required minlength="1"/>
          </label>
        </div>
        <div>
          <label>
            <p>E-mail</p>
            <input type="text" v-model="email" id="email" name="email" required/>
          </label>
        </div>
        <div>
          <label>
            <p>Topic</p>
            <select id="topic" v-model="topic" name="topic">
              <option>---</option>
              <option id="hi" value="Just wanna say hi">Just want to say hi</option>
              <option id="suggestion" value="Suggestion for site">Suggestion for site</option>
              <option id="date" value="I want to ask you out for a date">I want to ask you out for a date</option>
              <option id="dontKnow" value="I don't know where I am">I don't know where I am</option>
            </select>
          </label>
        </div>
        <div>
          <label>
            <p>Message</p>
            <textarea placeholder="Message" v-model="message" name="message" required id="message"></textarea>
          </label>
        </div>
        <input id="saveCredentials" type="checkbox" name="saveCredentials">
        <label for="saveCredentials">Save name and email?</label>
        <div><input type="submit" value="Send"/></div>
      </form>
    </div>
  </main>
</template>

<script>
export default {
  name: 'Contact',
  props: {},
  components: {
  },
  data() {
    return {
      displayForm: 'block',
      headerTextAlign: 'left',
      headerText: 'Contact me',
      name: null,
      email: null,
      topic: null,
      message: null
    }
  },
  methods: {
    async submitForm() {
      try {
        const queryParams = `name=${this.name}&email=${this.email}&topic=${this.topic}&message=${this.message}`
        const response = await fetch(`${window.location.protocol}//${window.location.hostname}:5000/backend/contact?${queryParams}`)
        if (response.status === 200) {
          this.displayForm = 'none'
          this.headerTextAlign = 'center'
          this.headerText = 'Thank you for contacting me!'
        } else {
          alert("Something went wrong")
        }
      } catch (error) {
        console.log(error)
      }
    }
  }
}
</script>

<style scoped>
main {
  width: 1000px;
}
p {
	margin: 1em 0 0.4em;
	padding-left: 2px;
}

input[type=text], select, textarea{
	width: 75%;
	padding: 5px 8px;
	border: 2px solid #ccc;
	border-radius: 4px;
	background: #f8f8f8;
	font-size: 14px;
}

@media (min-width: 620px) {
	input[type=text], select, textarea {
		width: 50%;
	}
}

#header {
  font-size: 40px;
  margin: 0;
}

textarea {
  height: 200px;
  resize: none;
}

</style>