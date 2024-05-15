<template>
  <v-layout class="rounded rounded-md">
    <HighBar/>
    <v-navigation-drawer>
      <left-bar
      @itemChoice="getChoice"/>
    </v-navigation-drawer>

    <v-main class="d-flex align-center justify-center" style="min-height: 300px;">
    </v-main>
  </v-layout>
</template>

<script setup>
  import {ref} from "vue";
  import HighBar from '@/components/Nav/HighBar.vue';
  import LeftBar from "@/components/Nav/LeftBar.vue";

  const selected_item = ref(0)

  const getChoice = (selectedValue) => {
    selected_item.value= selectedValue
  }




</script>
<style scoped>

*
{
  background: white;
}

</style>
