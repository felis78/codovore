<template>
    <v-card class="mx-auto pa-12 pb-8"
            elevation="8"
            max-width="448"
            rounded="lg"
    >
        <div class="text-subtitle-1 text-medium-emphasis">Account</div>
        <v-avatar ></v-avatar>
        <v-text-field
          width="290"
          v-model="email"
            density="compact"
            placeholder="Email"
            prepend-inner-icon=""
            variant="outlined"
        ></v-text-field>
      <div class="text-subtitle-1 text-medium-emphasis">Password</div>
        <v-text-field
          v-model="password"
        :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
        :type="visible ? 'text' : 'password'"
        density="compact"
        placeholder="Enter your password"
        prepend-inner-icon="mdi-lock-outline"
        variant="outlined"
        @click:append-inner="visible = !visible"
      ></v-text-field>
      <v-btn
        class="mb-8"
        color="blue"
        size="large"
        variant="tonal"
        block
        @click=send_login()
      >
        Log In
      </v-btn>
    </v-card>
</template>


<script setup>
import { ref } from 'vue';

let visible = ref(false)
let email = ref()
let password = ref()

async function send_login() {
  if (!email.value){
    alert("Email is required")
    return false
  }

  if (!password.value){
    alert("Password is required")
    return false
  }

  if (!verify_email(email.value)){
    alert("Correct email is required")
    return false
  }

  let url="http://localhost:5000/check_password"
  let response = await fetch(url, {
    method: 'POST',
    body: JSON.stringify({email: email.value,
                                password: password.value}),
    headers: {'Content-Type': 'application/json'}
  })
    console.log(response.status)
  if (response.status === 200){
    alert("OK")
    //using vuex for session managment
    return true
  }
  else {
    alert("Bad email or password")
    return false
  }
}

//verify if email content @
function verify_email(email) {
    let character = /[@]/
    return email.search(character) !== -1;
}

</script>
