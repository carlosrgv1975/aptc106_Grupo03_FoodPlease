import { Component, OnInit } from '@angular/core';
import { FoodpleaseApiService } from '../core/services/foodplease-api.service';
import { Pedido } from '../core/models/foodplease.models';

@Component({
  selector: 'app-tab2',
  templateUrl: 'tab2.page.html',
  styleUrls: ['tab2.page.scss'],
  standalone: false,
})
export class Tab2Page implements OnInit {
  pedidos: Pedido[] = [];
  cargando = true;
  error: string | null = null;

  constructor(private api: FoodpleaseApiService) {}

  ngOnInit(): void {
    this.cargarPedidos();
  }

  cargarPedidos(): void {
    this.cargando = true;
    this.error = null;
    this.api.getPedidos().subscribe({
      next: (data) => {
        this.pedidos = data;
        this.cargando = false;
      },
      error: (err) => {
        this.error = 'No fue posible cargar los pedidos. Verifica que el backend Flask esté corriendo.';
        this.cargando = false;
        console.error('Error al cargar pedidos:', err);
      },
    });
  }

  colorEstado(estado: string): string {
    switch (estado) {
      case 'Pendiente':
        return 'medium';
      case 'Preparando':
        return 'warning';
      case 'En ruta':
        return 'primary';
      case 'Entregado':
        return 'success';
      case 'Cancelado':
        return 'danger';
      default:
        return 'medium';
    }
  }

  iconoEstado(estado: string): string {
    switch (estado) {
      case 'Pendiente':
        return 'time-outline';
      case 'Preparando':
        return 'flame-outline';
      case 'En ruta':
        return 'bicycle-outline';
      case 'Entregado':
        return 'checkmark-done-circle-outline';
      case 'Cancelado':
        return 'close-circle-outline';
      default:
        return 'help-circle-outline';
    }
  }
}
