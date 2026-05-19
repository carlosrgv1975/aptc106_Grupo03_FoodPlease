/**
 * Modelos TypeScript del dominio FoodPlease.
 * Reflejan uno a uno las entidades del backend Flask (app/models.py).
 * Sirven como contrato entre la API REST y la app móvil.
 */

export interface Cliente {
  id: number;
  nombre: string;
  telefono: string;
  direccion: string;
  created_at?: string;
}

export interface Local {
  id: number;
  nombre: string;
  rubro: string;
  direccion: string;
  created_at?: string;
}

export interface Repartidor {
  id: number;
  nombre: string;
  telefono: string;
  vehiculo: string;
  disponible: boolean;
  created_at?: string;
}

export interface Pedido {
  id: number;
  descripcion: string;
  estado: 'Pendiente' | 'Preparando' | 'En ruta' | 'Entregado' | 'Cancelado';
  direccion_entrega: string;
  total: number;
  fecha_creacion?: string;
  cliente_id: number;
  local_id: number;
  repartidor_id: number | null;
  cliente?: Cliente;
  local?: Local;
  repartidor?: Repartidor;
}

export interface NuevoPedido {
  descripcion: string;
  direccion_entrega: string;
  total: number;
  estado?: string;
  cliente_id: number;
  local_id: number;
  repartidor_id?: number;
}

export interface Metrics {
  clientes: number;
  locales: number;
  repartidores: number;
  pedidos: number;
  pendientes: number;
  en_ruta: number;
  entregados: number;
}

export interface AuthResponse {
  token: string;
  cliente: Cliente;
}
