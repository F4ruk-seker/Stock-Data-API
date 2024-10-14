<template>
<main class="panel-main content-center justify-center p-0 md:p-5 overflow-hidden">
    <section class="shadow-sm shadow-cyan-800 backdrop-blur-sm max-h-full justify-center content-center rounded-md">
        <article>
            <AppHeader />
        </article>
        <article name="app">
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