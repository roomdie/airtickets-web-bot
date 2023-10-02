import {createRouter, createWebHashHistory} from "vue-router"
import MainPage from "@/pages/MainPage";
import TicketFindPage from "@/pages/TicketFindPage";

const routes = [
    {
        path: "/",
        component: MainPage,
    },
    {
        path: "/ticketFindPage",
        component: TicketFindPage,
    },
]

const router = createRouter({
    routes,
    history: createWebHashHistory()
    })

export default router;
