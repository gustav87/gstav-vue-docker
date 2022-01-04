import {createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue'
import Blog from '../views/Blog.vue'
import Playground from '../views/Playground.vue'
import Contact from '../views/Contact.vue'
import Colors from '../views/Colors.vue'
import GithubSearch from '../views/GithubSearch.vue'
import GithubUser from '../views/GithubUser.vue'
import Map from '../views/Map.vue'
import FlickrViewer from '../views/FlickrViewer.vue'
import VueStuff from '../views/VueStuff.vue'
import DbStuff from '../views/DbStuff.vue'
import JsStuff from '../views/JsStuff.vue'
import NotFound from '../views/NotFound.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/blog',
    name: 'Blog',
    component: Blog
  },
  {
    path: '/playground',
    name: 'Playground',
    component: Playground,
    children: [
      {
        path: 'colors',
        component: Colors
      },
      {
        path: 'map',
        component: Map
      },
      {
        path: 'flickrViewer',
        component: FlickrViewer
      },
      {
        path: 'dbStuff',
        component: DbStuff
      },
      {
        path: 'githubSearch',
        component: GithubSearch
      },
      {
        path: 'githubUser/:username',
        component: GithubUser
      }
    ]
  },
  {
    path: '/contact',
    name: 'Contact',
    component: Contact
  },
  {
    path: '/playground/vueStuff',
    name: 'vueStuff',
    component: VueStuff
  },
  {
    path: '/playground/jsStuff',
    name: 'JsStuff',
    component: JsStuff
  },
  {
    path: '/:catchAll(.*)',
    name: 'NotFound',
    component: NotFound
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
