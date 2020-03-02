import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Board from '../views/Board.vue'
import Post from '../views/Post.vue'
import PostWrite from '../views/PostWrite.vue'
import PostUpdate from '../views/PostUpdate.vue'
import notfound from '../views/404.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/board/:cat',
    name: 'Board',
    component: Board,
    beforeEnter: (to, from, next) => {
      if (to.params.cat === 'notice' || to.params.cat === 'community' || to.params.cat === 'questions' || to.params.cat === 'code') {
        next();
      }
      else {
        next('/404');
      }
    }
  },
  {
    path: '/board/post/:post_id/update',
    name: 'PostUpdate',
    component: PostUpdate
  },
  {
    path: '/board/post/:post_id',
    name: 'Post',
    component: Post
  },
  {
    path: '/board/:cat/write',
    name: 'postWrite',
    component: PostWrite,
    beforeEnter: (to, from, next) => {
      if (to.params.cat === 'notice' || to.params.cat === 'community' || to.params.cat === 'questions' || to.params.cat === 'code') {
        next();
      }
      else {
        next('/404');
      }
    }
  },
  {
    path:'*',
    redirect: '/404'
  },
  {
    path:'/404',
    component: notfound
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
