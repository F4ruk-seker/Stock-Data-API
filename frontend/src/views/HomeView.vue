<template>
  <div class="text-gray-50 font-semibold h-screen overflow-scroll">
  <table class="table table-zebra">
    <!-- head -->
    <thead class="text-gray-50 sticky top-0 z-10 ">
      <tr>
        <th></th>
        <th></th>
        <th>Code</th>
        <th>Title</th>
        <th>Price</th>
        <th>R</th>
        <th>Chart</th>
        <th>Edit</th>
        <th>Delete <button class="btn" @click="show=!show">show</button></th>
      </tr>
    </thead>
    <tbody v-if="show" class="">
      <!-- row 1 -->
      <tr>
        <th>1</th>
        <td><img class="min-h-[34px] max-h-[34px] min-w-[34px] max-w-[34px]" src="https://static.doviz.com/images/stock/THYAO.png"></td>
        <td>THYAO</td>
        <td>TURK HAVA YOLLARI</td>
        <td>264.75</td>
        <td>-0.66</td>
        <td><img class="min-h-[34px] max-h-[34px]" src="https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125"></td>
        <td><button class="btn btn-sm outline-cyan-300">Edit</button></td>
        <td><button class="btn btn-sm">Delete</button></td>
      </tr>
      <tr>
        <th>1</th>
        <td><img class="min-h-[34px] max-h-[34px] min-w-[34px] max-w-[34px]" src="https://static.doviz.com/images/stock/THYAO.png"></td>
        <td>THYAO</td>
        <td>TURK HAVA YOLLARI</td>
        <td>264.75</td>
        <td>-0.66</td>
        <td><img class="min-h-[34px] max-h-[34px]" src="https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125"></td>
        <td><button class="btn btn-sm outline-cyan-300">Edit</button></td>
        <td><button class="btn btn-sm">Delete</button></td>
      </tr><tr>
        <th>1</th>
        <td><img class="min-h-[34px] max-h-[34px] min-w-[34px] max-w-[34px]" src="https://static.doviz.com/images/stock/THYAO.png"></td>
        <td>THYAO</td>
        <td>TURK HAVA YOLLARI</td>
        <td>264.75</td>
        <td>-0.66</td>
        <td><img class="min-h-[34px] max-h-[34px]" src="https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125"></td>
        <td><button class="btn btn-sm outline-cyan-300">Edit</button></td>
        <td><button class="btn btn-sm">Delete</button></td>
      </tr><tr>
        <th>1</th>
        <td><img class="min-h-[34px] max-h-[34px] min-w-[34px] max-w-[34px]" src="https://static.doviz.com/images/stock/THYAO.png"></td>
        <td>THYAO</td>
        <td>TURK HAVA YOLLARI</td>
        <td>264.75</td>
        <td>-0.66</td>
        <td><img class="min-h-[34px] max-h-[34px]" src="https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125"></td>
        <td><button class="btn btn-sm outline-cyan-300">Edit</button></td>
        <td><button class="btn btn-sm">Delete</button></td>
      </tr><tr>
        <th>1</th>
        <td><img class="min-h-[34px] max-h-[34px] min-w-[34px] max-w-[34px]" src="https://static.doviz.com/images/stock/THYAO.png"></td>
        <td>THYAO</td>
        <td>TURK HAVA YOLLARI</td>
        <td>264.75</td>
        <td>-0.66</td>
        <td><img class="min-h-[34px] max-h-[34px]" src="https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125"></td>
        <td><button class="btn btn-sm outline-cyan-300">Edit</button></td>
        <td><button class="btn btn-sm">Delete</button></td>
      </tr><tr>
        <th>1</th>
        <td><img class="min-h-[34px] max-h-[34px] min-w-[34px] max-w-[34px]" src="https://static.doviz.com/images/stock/THYAO.png"></td>
        <td>THYAO</td>
        <td>TURK HAVA YOLLARI</td>
        <td>264.75</td>
        <td>-0.66</td>
        <td><img class="min-h-[34px] max-h-[34px]" src="https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125"></td>
        <td><button class="btn btn-sm outline-cyan-300">Edit</button></td>
        <td><button class="btn btn-sm">Delete</button></td>
      </tr><tr>
        <th>1</th>
        <td><img class="min-h-[34px] max-h-[34px] min-w-[34px] max-w-[34px]" src="https://static.doviz.com/images/stock/THYAO.png"></td>
        <td>THYAO</td>
        <td>TURK HAVA YOLLARI</td>
        <td>264.75</td>
        <td>-0.66</td>
        <td><img class="min-h-[34px] max-h-[34px]" src="https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125"></td>
        <td><button class="btn btn-sm outline-cyan-300">Edit</button></td>
        <td><button class="btn btn-sm">Delete</button></td>
      </tr><tr>
        <th>1</th>
        <td><img class="min-h-[34px] max-h-[34px] min-w-[34px] max-w-[34px]" src="https://static.doviz.com/images/stock/THYAO.png"></td>
        <td>THYAO</td>
        <td>TURK HAVA YOLLARI</td>
        <td>264.75</td>
        <td>-0.66</td>
        <td><img class="min-h-[34px] max-h-[34px]" src="https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125"></td>
        <td><button class="btn btn-sm outline-cyan-300">Edit</button></td>
        <td><button class="btn btn-sm">Delete</button></td>
      </tr><tr>
        <th>1</th>
        <td><img class="min-h-[34px] max-h-[34px] min-w-[34px] max-w-[34px]" src="https://static.doviz.com/images/stock/THYAO.png"></td>
        <td>THYAO</td>
        <td>TURK HAVA YOLLARI</td>
        <td>264.75</td>
        <td>-0.66</td>
        <td><img class="min-h-[34px] max-h-[34px]" src="https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125"></td>
        <td><button class="btn btn-sm outline-cyan-300">Edit</button></td>
        <td><button class="btn btn-sm">Delete</button></td>
      </tr><tr>
        <th>1</th>
        <td><img class="min-h-[34px] max-h-[34px] min-w-[34px] max-w-[34px]" src="https://static.doviz.com/images/stock/THYAO.png"></td>
        <td>THYAO</td>
        <td>TURK HAVA YOLLARI</td>
        <td>264.75</td>
        <td>-0.66</td>
        <td><img class="min-h-[34px] max-h-[34px]" src="https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125"></td>
        <td><button class="btn btn-sm outline-cyan-300">Edit</button></td>
        <td><button class="btn btn-sm">Delete</button></td>
      </tr><tr>
        <th>1</th>
        <td><img class="min-h-[34px] max-h-[34px] min-w-[34px] max-w-[34px]" src="https://static.doviz.com/images/stock/THYAO.png"></td>
        <td>THYAO</td>
        <td>TURK HAVA YOLLARI</td>
        <td>264.75</td>
        <td>-0.66</td>
        <td><img class="min-h-[34px] max-h-[34px]" src="https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125"></td>
        <td><button class="btn btn-sm outline-cyan-300">Edit</button></td>
        <td><button class="btn btn-sm">Delete</button></td>
      </tr><tr>
        <th>1</th>
        <td><img class="min-h-[34px] max-h-[34px] min-w-[34px] max-w-[34px]" src="https://static.doviz.com/images/stock/THYAO.png"></td>
        <td>THYAO</td>
        <td>TURK HAVA YOLLARI</td>
        <td>264.75</td>
        <td>-0.66</td>
        <td><img class="min-h-[34px] max-h-[34px]" src="https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125"></td>
        <td><button class="btn btn-sm outline-cyan-300">Edit</button></td>
        <td><button class="btn btn-sm">Delete</button></td>
      </tr><tr>
        <th>1</th>
        <td><img class="min-h-[34px] max-h-[34px] min-w-[34px] max-w-[34px]" src="https://static.doviz.com/images/stock/THYAO.png"></td>
        <td>THYAO</td>
        <td>TURK HAVA YOLLARI</td>
        <td>264.75</td>
        <td>-0.66</td>
        <td><img class="min-h-[34px] max-h-[34px]" src="https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125"></td>
        <td><button class="btn btn-sm outline-cyan-300">Edit</button></td>
        <td><button class="btn btn-sm">Delete</button></td>
      </tr><tr>
        <th>1</th>
        <td><img class="min-h-[34px] max-h-[34px] min-w-[34px] max-w-[34px]" src="https://static.doviz.com/images/stock/THYAO.png"></td>
        <td>THYAO</td>
        <td>TURK HAVA YOLLARI</td>
        <td>264.75</td>
        <td>-0.66</td>
        <td><img class="min-h-[34px] max-h-[34px]" src="https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125"></td>
        <td><button class="btn btn-sm outline-cyan-300">Edit</button></td>
        <td><button class="btn btn-sm">Delete</button></td>
      </tr><tr>
        <th>1</th>
        <td><img class="min-h-[34px] max-h-[34px] min-w-[34px] max-w-[34px]" src="https://static.doviz.com/images/stock/THYAO.png"></td>
        <td>THYAO</td>
        <td>TURK HAVA YOLLARI</td>
        <td>264.75</td>
        <td>-0.66</td>
        <td><img class="min-h-[34px] max-h-[34px]" src="https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125"></td>
        <td><button class="btn btn-sm outline-cyan-300">Edit</button></td>
        <td><button class="btn btn-sm">Delete</button></td>
      </tr><tr>
        <th>1</th>
        <td><img class="min-h-[34px] max-h-[34px] min-w-[34px] max-w-[34px]" src="https://static.doviz.com/images/stock/THYAO.png"></td>
        <td>THYAO</td>
        <td>TURK HAVA YOLLARI</td>
        <td>264.75</td>
        <td>-0.66</td>
        <td><img class="min-h-[34px] max-h-[34px]" src="https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125"></td>
        <td><button class="btn btn-sm outline-cyan-300">Edit</button></td>
        <td><button class="btn btn-sm">Delete</button></td>
      </tr><tr>
        <th>1</th>
        <td><img class="min-h-[34px] max-h-[34px] min-w-[34px] max-w-[34px]" src="https://static.doviz.com/images/stock/THYAO.png"></td>
        <td>THYAO</td>
        <td>TURK HAVA YOLLARI</td>
        <td>264.75</td>
        <td>-0.66</td>
        <td><img class="min-h-[34px] max-h-[34px]" src="https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125"></td>
        <td><button class="btn btn-sm outline-cyan-300">Edit</button></td>
        <td><button class="btn btn-sm">Delete</button></td>
      </tr><tr>
        <th>1</th>
        <td><img class="min-h-[34px] max-h-[34px] min-w-[34px] max-w-[34px]" src="https://static.doviz.com/images/stock/THYAO.png"></td>
        <td>THYAO</td>
        <td>TURK HAVA YOLLARI</td>
        <td>264.75</td>
        <td>-0.66</td>
        <td><img class="min-h-[34px] max-h-[34px]" src="https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125"></td>
        <td><button class="btn btn-sm outline-cyan-300">Edit</button></td>
        <td><button class="btn btn-sm">Delete</button></td>
      </tr><tr>
        <th>1</th>
        <td><img class="min-h-[34px] max-h-[34px] min-w-[34px] max-w-[34px]" src="https://static.doviz.com/images/stock/THYAO.png"></td>
        <td>THYAO</td>
        <td>TURK HAVA YOLLARI</td>
        <td>264.75</td>
        <td>-0.66</td>
        <td><img class="min-h-[34px] max-h-[34px]" src="https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125"></td>
        <td><button class="btn btn-sm outline-cyan-300">Edit</button></td>
        <td><button class="btn btn-sm">Delete</button></td>
      </tr><tr>
        <th>1</th>
        <td><img class="min-h-[34px] max-h-[34px] min-w-[34px] max-w-[34px]" src="https://static.doviz.com/images/stock/THYAO.png"></td>
        <td>THYAO</td>
        <td>TURK HAVA YOLLARI</td>
        <td>264.75</td>
        <td>-0.66</td>
        <td><img class="min-h-[34px] max-h-[34px]" src="https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125"></td>
        <td><button class="btn btn-sm outline-cyan-300">Edit</button></td>
        <td><button class="btn btn-sm">Delete</button></td>
      </tr><tr>
        <th>1</th>
        <td><img class="min-h-[34px] max-h-[34px] min-w-[34px] max-w-[34px]" src="https://static.doviz.com/images/stock/THYAO.png"></td>
        <td>THYAO</td>
        <td>SLOT</td>
        <td>264.75</td>
        <td>-0.66</td>
        <td><img class="min-h-[34px] max-h-[34px]" src="https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125"></td>
        <td><button class="btn btn-sm outline-cyan-300">Edit</button></td>
        <td><button class="btn btn-sm">Delete</button></td>
      </tr>
    </tbody>
  </table>
</div>
</template>

<script setup>
import { ref } from 'vue';

const show = ref(false)
/*
    {
        "id": 1,
        "asset": {
            "code": "THYAO",
            "name": "TURK HAVA YOLLARI",
            "current_price": "264.75",
            "max_price": "271.00",
            "min_price": "263.75",
            "percentage": "-0.66",
            "logo": "https://static.doviz.com/images/stock/THYAO.png",
            "url": "https://borsa.doviz.com/hisseler/thyao-turk-hava-yollari",
            "chart": "https://static.doviz.com/images/sparkline/THYAO.svg?t=1728803125",
            "created_at": "2024-09-08T11:26:16.906842+03:00",
            "updated_at": "2024-10-13T10:06:58.495924+03:00"
        },
        "slots": [
            {
                "id": 1,
                "progres_type": "buy",
                "price": "12.00",
                "quantity": 2
            },
            {
                "id": 2,
                "progres_type": "t_sale",
                "price": "120.00",
                "quantity": 1
            }
        ],
        "general_status": {
            "total_profit": "384.75",
            "remaining_lots": 1.0
        },
        "tracking": true,
        "owner": 1
    }
*/
</script>
