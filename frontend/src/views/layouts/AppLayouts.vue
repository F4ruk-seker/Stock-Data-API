<template>
<main class="panel-main h-screen overflow-hidden md:p-8">
    <section class="grid shadow-sm shadow-cyan-800 backdrop-blur-sm rounded-md border border-red-500 h-full">
        <article class="min-h-max">
           <AppHeader />
        </article>
        <article name="app" class="h-full overflow-x-auto rounded-md relative">
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