<script setup>
import {ref, defineEmits,watchEffect} from "vue";

const emit = defineEmits(["itemChoice"])

function emitChoice(value){
  emit("itemChoice", value);
}

</script>

<template>
  <v-list>
    <v-divider></v-divider>
    <v-list-item title="Présentation" @click="emitChoice(0)"></v-list-item>
    <v-divider></v-divider>
    <v-list-item title="Full CV" @click="emitChoice(1)"></v-list-item>
    <v-divider></v-divider>
    <v-list-item title="Détail formation" @click="emitChoice(2)"></v-list-item>
    <v-divider></v-divider>
    <v-list-item title="Détail posts" @click="emitChoice(3)"></v-list-item>
    <v-divider></v-divider>
    <v-list-item title="Détail professionals projects" @click="emitChoice(4)"></v-list-item>
    <v-divider></v-divider>
    <v-list-item title="Détail personals projects" @click="emitChoice(5)"></v-list-item>
    <v-divider></v-divider>
    <v-list-item title="Contacts" @click="emitChoice(6)"></v-list-item>
    <v-divider></v-divider>
  </v-list>
</template>

<style scoped>

</style>
