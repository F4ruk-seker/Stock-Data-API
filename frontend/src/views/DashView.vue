<template>
<AssetsTable :assets="assets_list" />
</template>

<script setup>
import AssetsTable from '@/components/AssetsTable.vue';
import { ref } from 'vue';
const assets_list = ref([
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
])
</script>