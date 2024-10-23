<template>
<main class="panel-main h-screen overflow-hidden p-0 sm:p-6 md:p-8 font-mono">
    <section class="grid shadow-lg backdrop-blur rounded-md h-full grid-rows-[auto,1fr]">
        <article class="h-auto ">
           <AppHeader />
        </article>
        <article name="app" class="min-h-full max-h-full overflow-x-auto rounded-md relative flex-1 flex-wrap grid-cols-1">
            <slot>
                slot in
            </slot>
        </article>
    </section>
</main>

</template>

<script setup>
import AppHeader from "@/components/AppHeader.vue";

</script>

<style>
.panel-main {
  height: 100vh;
  background-color: #413f3f4b!important;
  background-image: url('@/assets/app-bg.jpg');
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
}

/* width */
::-webkit-scrollbar {
  width: 10px;
}

/* Track */
::-webkit-scrollbar-track {
  background: #f1f1f123;
  /*border-radius: 5px;*/
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #88888881;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #5353536e;
}
</style>