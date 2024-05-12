<template>
  <v-layout class="rounded rounded-md">
    <HighBar/>
    <v-navigation-drawer>
      <v-list>
        <v-list-item title="Navigation drawer"></v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main class="d-flex align-center justify-center" style="min-height: 300px;">
    </v-main>
  </v-layout>
</template>

<script setup>
  import HighBar from './components/HighBar.vue'
</script>
<style scoped>

*
{
  background: white;
}

</style>
