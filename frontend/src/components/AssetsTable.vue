<template>
    <div class="mx-auto p-4">
      <table class="min-w-full table-auto table-zebra">
        <thead>
          <tr class="bg-gray-200 text-left">
            <th class="px-4 py-2">Code</th>
            <th class="px-4 py-2">Name</th>
            <th class="px-4 py-2">Current Price</th>
            <th class="px-4 py-2">Percentage Change</th>
            <th class="px-4 py-2">Logo</th>
            <th class="px-4 py-2">URL</th>
            <th class="px-4 py-2">Chart</th>
            <th class="px-4 py-2"></th>
          </tr>
        </thead>
        <tbody class="font-bold">
          <template v-for="(asset, index) in assets" :key="index">
            <tr class="odd:bg-gray-100 odd:hover:bg-gray-200 even:hover:bg-gray-200">
                <td class="px-4 py-2">{{ asset.asset.code }}</td>
                <td class="px-4 py-2">{{ asset.asset.name }}</td>
                <td class="px-4 py-2">{{ asset.asset.current_price }}</td>
                <td :class="[asset.asset.percentage < 0 ? 'text-red-500' : 'text-green-500']" class="px-4 py-2">{{ asset.asset.percentage }}</td>
                <td class="px-4 py-2"><img :src="asset.asset.logo" alt="Logo" class="w-8 h-8"></td>
                <td class="px-4 py-2"><a :href="asset.asset.url" target="_blank" class="text-blue-500">Link</a></td>
                <td class="px-4 py-2"><img :src="asset.asset.chart" alt="Chart" class="w-16 h-8"></td>
                <td class="px-4 py-2"><button @click="asset.expend=!asset.expend">history log</button></td>
            </tr>
            <tr v-show="asset.expend">
                <td colspan="2"></td>
                <td style="background-color: #ffffff63;" colspan="6">pars</td>
            </tr>
            <tr class="hidden"></tr>
          </template>
        
        </tbody>
      </table>
    </div>
  </template>
  
<style scoped>
/*
tr:nth-child(odd) {background-color: #ecececa9}
tr:nth-child(even) {background-color: #1616167c!important}
*/
</style>

  <script setup>
  import { ref } from 'vue';
  
  const assets = ref([
  {
      asset: {
        code: "THYAO",
        name: "TURK HAVA YOLLARI",
        current_price: "264.75",
        percentage: "-0.66",
        logo: "https://static.doviz.com/images/stock/THYAO.png",
        url: "https://borsa.doviz.com/hisseler/thyao-turk-hava-yollari",
        chart: "https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125",
      },
      general_status: {
        total_profit: "384.75",
        remaining_lots: 1.0
      },
      tracking: true,
      owner: 1,
      expend: false
    }, {
      asset: {
        code: "THYAO",
        name: "TURK HAVA YOLLARI",
        current_price: "264.75",
        percentage: "-0.66",
        logo: "https://static.doviz.com/images/stock/THYAO.png",
        url: "https://borsa.doviz.com/hisseler/thyao-turk-hava-yollari",
        chart: "https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125",
      },
      general_status: {
        total_profit: "384.75",
        remaining_lots: 1.0
      },
      tracking: true,
      owner: 1,
      expend: false
    }, {
      asset: {
        code: "THYAO",
        name: "TURK HAVA YOLLARI",
        current_price: "264.75",
        percentage: "-0.66",
        logo: "https://static.doviz.com/images/stock/THYAO.png",
        url: "https://borsa.doviz.com/hisseler/thyao-turk-hava-yollari",
        chart: "https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125",
      },
      general_status: {
        total_profit: "384.75",
        remaining_lots: 1.0
      },
      tracking: true,
      owner: 1,
      expend: false
    }, {
      asset: {
        code: "THYAO",
        name: "TURK HAVA YOLLARI",
        current_price: "264.75",
        percentage: "-0.66",
        logo: "https://static.doviz.com/images/stock/THYAO.png",
        url: "https://borsa.doviz.com/hisseler/thyao-turk-hava-yollari",
        chart: "https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125",
      },
      general_status: {
        total_profit: "384.75",
        remaining_lots: 1.0
      },
      tracking: true,
      owner: 1,
      expend: false
    }, {
      asset: {
        code: "THYAO",
        name: "TURK HAVA YOLLARI",
        current_price: "264.75",
        percentage: "-0.66",
        logo: "https://static.doviz.com/images/stock/THYAO.png",
        url: "https://borsa.doviz.com/hisseler/thyao-turk-hava-yollari",
        chart: "https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125",
      },
      general_status: {
        total_profit: "384.75",
        remaining_lots: 1.0
      },
      tracking: true,
      owner: 1,
      expend: false
    },
  ]);
  </script>