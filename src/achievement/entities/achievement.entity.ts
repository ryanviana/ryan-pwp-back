import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { HydratedDocument } from 'mongoose';

export type AchievementDocument = HydratedDocument<Achievement>;

@Schema({ timestamps: true })
export class Achievement {
  @Prop({ required: true })
  title: string;

  @Prop({ required: true })
  organization: string;

  @Prop({ required: true })
  date: string;

  @Prop({ required: true })
  description: string;
}

export const AchievementSchema = SchemaFactory.createForClass(Achievement);
