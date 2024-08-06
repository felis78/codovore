<template>

  <canvas aria-label="Canva de titre" ref="canvasTitle" width="445" height="40"></canvas>

</template>

<script setup lang="ts">

import {ref, onMounted } from "vue";

let canvasTitle = ref<HTMLCanvasElement>()

onMounted(() => {
  const canvas = <object> canvasTitle.value;
  const ctx = <CanvasRenderingContext2D> canvas.getContext("2d");
  const letters:Array<string> = ["{Co", "do", "vo", "re", ".fr}" ];
  const colors:Array<string> =  ['#ADD8E6', '#7FFFD4', '#40E0D0', '#20B2AA', '#0D98BA', '#008080', '#006666', '#004D40', '#003366', '#001A66']
  let position:number = 0;
  ctx.font = "38px serif"
  ctx.textBaseline = "middle";


  function printLetters(items:Array<string>, delay:number ){
    let index:number = 0


    function processItem() {
      if (index >= items.length) {
        return;
      }

      // Traiter l'élément actuel
      ctx.fillStyle=colors[index]

      ctx.fillText(letters[index], position <= 92 ? position += 92 : position += 60 , 100)
      setTimeout(() => {
        index++; // Incrémenter l'index pour passer à l'élément suivant
        processItem(); // Appeler récursivement processItem pour traiter l'élément suivant
      }, delay);
    }
    processItem();
  }

  printLetters(letters, 200)

  // Commencer le traitement avec le premier élément
})
</script>

<style scoped>



</style>
