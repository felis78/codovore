import { createMemoryHistory, createRouter } from 'vue-router'
import SignUp from '@/components/users/SignUp.vue'
import SignIn from "@/components/users/SignIn.vue";

const routes = [
  { path: '/signin', component: SignIn },
  { path: '/signup', component: SignUp },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router
