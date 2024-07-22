<template>
  <v-layout class="rounded rounded-md">
    <HighBar
    @login="logging"/>
    <v-navigation-drawer>
      <left-bar
      @itemChoice="getChoice"/>
    </v-navigation-drawer>

    <v-main class="d-flex align-center justify-center" style="min-height: 300px;">

      <SignIn v-if="login===true"/>
      <formation v-if="selected_item===2"/>
      <DetailPosts v-if="selected_item===3"/>
      <contact v-if="selected_item===6"/>
    </v-main>

  </v-layout>
</template>

<script setup>
  import {ref} from "vue";
  import HighBar from '@/components/Nav/HighBar.vue';
  import LeftBar from "@/components/Nav/LeftBar.vue";
  import Contact from "@/components/selected_Page/Contact.vue";
  import Formation from "@/components/selected_Page/Formation.vue";
  import DetailPosts from "@/components/selected_Page/DetailPosts.vue";
  import FullCV from "@/components/selected_Page/FullCV.vue";
  import SignIn from "./components/users/SignIn.vue";

  const selected_item = ref(0)
  const login = ref(false)
  const getChoice = (selectedValue) => {
    selected_item.value= selectedValue
    login.value = false
  }

  const logging = (loging_value) => {
    login.value = loging_value
    selected_item.value = 0
  }





</script>

<style scoped>



</style>
