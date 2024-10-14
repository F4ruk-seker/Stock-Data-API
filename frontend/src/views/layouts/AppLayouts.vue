<template>
<section class="panel-main flex content-center justify-center p-0 md:p-5">
    <article name="app" class="w-full m-5 p-2 shadow-sm shadow-cyan-800 backdrop-blur-sm justify-center content-center rounded-md">
        <slot>
            slot in
        </slot>
    </article>
</section>
</template>

<script setup>
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