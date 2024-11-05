import axios from '../plugins/axios'; // Plugin olarak axios'u dahil edin


class AssetService {
    async get_mine(){
        return await(await axios.get('http://127.0.0.1:8000/api/assets/mine')).data 
    }
}

export default new AssetService();