import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/dash',
    name: 'dash',
    component: () => import(/* webpackChunkName: "about" */ '../views/DashView.vue'),
    meta: {
      requiresAuth: false, // auth example
    },
  },
  // {
  //   path: 'app',
  //   name: 'app',
  //   // component: () => import(/* webpackChunkName: "auth" */ '../views/blog/BlogView.vue'),
  //   children: [
  //     // {
  //     //   path: '',
  //     //   name: 'blog-list',
  //     //   component: () => import(/* webpackChunkName: "login" */ '../views/blog/BlogsListView.vue')
  //     // },      {
  //     //   path: ':slug',
  //     //   name: 'blog-content',
  //     //   component: () => import(/* webpackChunkName: "register" */ '../views/blog/BlogContentView.vue'),
  //     //   props: true
  //     // }
  //   ]
  // },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  linkActiveClass: "active", // active class for non-exact links.
  linkExactActiveClass: "active" // active class for *exact* links.
})

export default router
