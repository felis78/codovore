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
          <v-app-bar-title
            class="d-flex align-center justify-center"
            text="Codovore.fr"></v-app-bar-title>
          <v-spacer>
          </v-spacer>
          <v-btn @click="login(true)"> Login </v-btn>
          <v-btn> Sign In </v-btn>
    </v-app-bar>
</template>
<script setup>

const emit= defineEmits(["login"]);

function login(logging){
  emit("login",logging);
}


</script>
