<template>
    <v-app-bar
      color="whit"
      background-color="white"
      density="comfortable"
      height="50"
      elevation = "2">
      <template v-slot:prepend>
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
      </template>

          <BigTitle/>
          <v-spacer>
          </v-spacer>
          <v-btn @click="login(true)"> Login </v-btn>
          <v-btn> Sign In </v-btn>
    </v-app-bar>
</template>
<script setup lang="ts">

import BigTitle from "@/components/Nav/BigTitle.vue";

const emit= defineEmits<{"login":[value: boolean]}>();

function login(logging: boolean ){
  emit("login",logging);
}


</script>
