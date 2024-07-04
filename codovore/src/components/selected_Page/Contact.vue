<script setup>

import {ref} from "vue";


</script>

<template>
  <v-col>
    <v-card
      class="card"
      width="20rem"
      height="auto"
      >
    <v-row>
  <FormKit
    class="form"
    type="form"
    nam="contact"
    :value="{
      nom: 'Regine',
      prenom: 'Poirier',
      poste: 'Recruteur',
      message: 'Ecrivez votre message'
    }">

    <FormKit
      class="form"
      type="text"
      name="nom"
      label="Nom"
    >
    </formKit>
    <formKit
      name="prenom"
      label="Prenom"
    />
    <formKit
      name="poste"
      label="Poste"
    />
</FormKit>
      </v-row>
  </v-card>
  </v-col>
</template>

<style scoped>

card
{
  padding: 1rem;
}

form
{
  margin: 2rem auto;
}

</style>
