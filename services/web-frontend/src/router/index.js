import {createRouter, createWebHistory} from "vue-router"
import MainPage from "@/pages/MainPage";
import TicketFindPage from "@/pages/search/SearchTicketsPage";
import TicketsPage from "@/pages/search/AvailableTicketsPage";
import PrePaymentPage from "@/pages/payment/PrePaymentPage";
import SuccessfulPaidPage from "@/pages/payment/SuccessfulPaidPage";
import PurchasedTicketsPage from "@/pages/purchased/PurchasedTicketsPage";
import TicketQrCodePage from "@/pages/purchased/TicketQrCodePage";
import QrLinkPage from "@/pages/purchased/LinkToQrCodePage";
import FailedPaidPage from "@/pages/payment/FailedPaidPage";


const routes = [
    {
        path: "/",
        component: MainPage,
    },
    {
        path: "/ticketFind",
        component: TicketFindPage,
    },
    {
        path: "/searchTickets",
        component: TicketsPage,
    },
    {
        path: "/purchasedTickets",
        component: PurchasedTicketsPage,
    },
    {
        path: "/prePayment",
        component: PrePaymentPage,
    },
    {
        path: "/successfulPaid",
        component: SuccessfulPaidPage,
    },
    {
        path: "/failedPaid",
        component: FailedPaidPage,
    },
    {
        path: "/ticketQrCode",
        component: TicketQrCodePage,
    },

    {
        path: "/qrLink",
        component: QrLinkPage,
    },


]

const router = createRouter({
    routes,
    history: createWebHistory()
    })

export default router;
