<template>
  <main id="flickrViewerPage">
    <p>Use the flickr API</p>
    <label for="flickrTag">Input image tag</label>
    <input type="text" v-model="tag" name="flickrTag" id="flickrTag" v-on:keyup.enter="getTaggedImages">
    <br>
    <button type="button" id="flickrImages" @click="getTaggedImages">Search for tagged images</button>
    <button type="button" id="flickrDogs" @click="getDogs">Look at dogs</button>

    <p>{{err}}</p>
    <div v-if="showDogs" v-for="p in dogs">
      <p>{{p.title}}</p>
      <img :src="getDogImgSrc(p)">
    </div>

    <div v-if="showTaggedImages" v-for="p in taggedImages">
      <p>{{p.title}}</p>
      <img :src="getTaggedImgSrc(p)">
    </div>
  </main>
</template>

<script>
export default {
  name: 'FlickrViewer',
  components: {
  },
  data() {
    return {
      showDogs: false,
      showTaggedImages: false,
      tag: '',
      err: null
    }
  },
  methods: {
    async getDogs() {
      try {
        const response = await fetch(`${window.location.protocol}//${window.location.hostname}:5000/backend/flickr/getDogs`)
        if (response.status === 200) {
          const data = await response.json()
          this.dogs = data.photos.photo
          this.showDogs = true
          this.showTaggedImages = false
        } else {
          alert("Something went wrong")
        }
      } catch (error) {
        console.log(error)
      }
    },
    getDogImgSrc(p) {
      return `https://farm${p.farm}.staticflickr.com/${p.server}/${p.id}_${p.secret}.jpg`
    },
    async getTaggedImages() {
      try {
        const response = await fetch(`${window.location.protocol}//${window.location.hostname}:5000/backend/flickr/getTaggedImages?tag=${this.tag}`)
        if (response.status === 200) {
          const data = await response.json()
          this.taggedImages = data.photos.photo
          this.showDogs = false
          this.showTaggedImages = true
        } else {
          alert("Something went wrong")
        }
      } catch (error) {
        console.log(error)
      }
    },
    getTaggedImgSrc(p) {
      return `https://live.staticflickr.com/${p.server}/${p.id}_${p.secret}.jpg`
    }
  }
}
</script>

<style scoped>
div p {
   margin-top: 10px;
   margin-bottom: 5px;
}

img {
  max-width: 100%;
}
</style>
