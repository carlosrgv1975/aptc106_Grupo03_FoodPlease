/**
 * Servicio Angular que encapsula todas las llamadas HTTP a la API REST del backend Flask.
 *
 * Aplica el patrón Service Layer de Angular: cada componente inyecta este servicio
 * y consume métodos de alto nivel sin preocuparse por las URLs ni el manejo HTTP.
 *
 * Espeja el Service Layer del backend (PedidoService, DashboardService) para
 * mantener simetría arquitectónica entre web (Flask) y móvil (Ionic).
 */

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { environment } from '../../../environments/environment';
import {
  Cliente,
  Local,
  Repartidor,
  Pedido,
  NuevoPedido,
  Metrics,
  AuthResponse,
} from '../models/foodplease.models';

@Injectable({
  providedIn: 'root',
})
export class FoodpleaseApiService {
  private readonly baseUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  // ---------------- Health & Métricas ----------------

  health(): Observable<{ status: string; service: string; version: string }> {
    return this.http.get<{ status: string; service: string; version: string }>(
      `${this.baseUrl}/health`,
    );
  }

  getMetrics(): Observable<Metrics> {
    return this.http.get<Metrics>(`${this.baseUrl}/metrics`);
  }

  // ---------------- Auth ----------------

  login(email?: string, telefono?: string): Observable<AuthResponse> {
    return this.http.post<AuthResponse>(`${this.baseUrl}/auth/login`, {
      email,
      telefono,
    });
  }

  register(data: {
    nombre: string;
    telefono: string;
    direccion: string;
  }): Observable<AuthResponse> {
    return this.http.post<AuthResponse>(`${this.baseUrl}/auth/register`, data);
  }

  // ---------------- Clientes ----------------

  getClientes(): Observable<Cliente[]> {
    return this.http.get<Cliente[]>(`${this.baseUrl}/clientes`);
  }

  getCliente(id: number): Observable<Cliente> {
    return this.http.get<Cliente>(`${this.baseUrl}/clientes/${id}`);
  }

  // ---------------- Locales (restaurantes) ----------------

  getLocales(): Observable<Local[]> {
    return this.http.get<Local[]>(`${this.baseUrl}/locales`);
  }

  getLocal(id: number): Observable<Local> {
    return this.http.get<Local>(`${this.baseUrl}/locales/${id}`);
  }

  // ---------------- Repartidores ----------------

  getRepartidores(): Observable<Repartidor[]> {
    return this.http.get<Repartidor[]>(`${this.baseUrl}/repartidores`);
  }

  getRepartidoresDisponibles(): Observable<Repartidor[]> {
    return this.http.get<Repartidor[]>(`${this.baseUrl}/repartidores/disponibles`);
  }

  // ---------------- Pedidos ----------------

  getPedidos(): Observable<Pedido[]> {
    return this.http.get<Pedido[]>(`${this.baseUrl}/pedidos`);
  }

  getPedido(id: number): Observable<Pedido> {
    return this.http.get<Pedido>(`${this.baseUrl}/pedidos/${id}`);
  }

  getPedidosPorCliente(clienteId: number): Observable<Pedido[]> {
    return this.http.get<Pedido[]>(`${this.baseUrl}/pedidos/cliente/${clienteId}`);
  }

  crearPedido(payload: NuevoPedido): Observable<Pedido> {
    return this.http.post<Pedido>(`${this.baseUrl}/pedidos`, payload);
  }

  actualizarPedido(id: number, payload: NuevoPedido): Observable<Pedido> {
    return this.http.put<Pedido>(`${this.baseUrl}/pedidos/${id}`, payload);
  }

  actualizarEstadoPedido(id: number, estado: string): Observable<Pedido> {
    return this.http.patch<Pedido>(`${this.baseUrl}/pedidos/${id}/estado`, { estado });
  }

  eliminarPedido(id: number): Observable<void> {
    return this.http.delete<void>(`${this.baseUrl}/pedidos/${id}`);
  }

  getEstadosValidos(): Observable<{ estados: string[] }> {
    return this.http.get<{ estados: string[] }>(`${this.baseUrl}/pedidos/estados`);
  }
}
